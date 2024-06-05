import os
import pandas as pd
import argparse
import logging
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI
from llama_index import Document
import re
import dotenv
from tqdm.auto import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.exceptions import RequestException
import uuid

# Load environment variables from .env file
dotenv.load_dotenv()

# Configure the logging system
logging.basicConfig(filename='process_pinecone.log',  # Log file path
                    filemode='w',  # 'a' for append, 'w' for overwrite
                    format='%(asctime)s - %(levelname)s - %(message)s',  # Format of log messages
                    level=logging.INFO)  # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# Initialize Pinecone
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

# Initialize OpenAI
oai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

EMBEDDING_MODEL = os.getenv('OPENAI_EMBEDDING_MODEL', "text-embedding-3-small")

def embed_document(text, model=EMBEDDING_MODEL):
    """Embeds a single text document using the specified model."""
    if not text:
        logging.warning("Empty text received for embedding.")
        return None
    try:
        return oai.embeddings.create(input=[text], model=model).data[0].embedding
    except RequestException as e:
        logging.error(f"RequestException during embedding: {e}")
        return None
    except Exception as e:
        logging.error(f"Error embedding document: {e}")
        return None

def embed_documents(texts, model=EMBEDDING_MODEL, max_workers=10):
    """Embeds a list of text documents using the specified model in parallel."""
    embeddings = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(embed_document, text, model): text for text in texts}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Embedding documents"):
            try:
                result = future.result()
                if result is not None:
                    embeddings.append(result)
            except Exception as e:
                logging.error(f"Error embedding document: {e}")
    return embeddings

def normalize_whitespace(text):
    """Normalizes the whitespace in a text document."""
    return re.sub(r'\s+', ' ', text).strip()

def maybe_truncate_text(text, max_words=None):
    """Truncates the text if it exceeds the specified maximum number of words."""
    if max_words is not None:
        words = text.split()
        if len(words) > max_words:
            return " ".join(words[:max_words])
    return text

def divide_string_with_overlap(text, chunk_size=50, overlap=10):
    """Divides a string into chunks with a specified size and overlap."""
    words = text.split()
    if len(words) < chunk_size:
        return [text]

    chunks = []
    i = 0
    while i + chunk_size <= len(words):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        i += (chunk_size - overlap)

    if i < len(words):
        last_chunk = " ".join(words[-chunk_size:])
        if last_chunk not in chunks:
            chunks.append(last_chunk)

    return chunks

def process_csv(csv_file, file_folder, max_words=None, chunk_size=50, overlap=10):
    """Processes a CSV file and returns a list of Document objects."""
    df = pd.read_csv(csv_file)
    valid_documents = []

    for _, row in df.iterrows():
        file_path = os.path.join(file_folder, row['filename'])
        if not os.path.exists(file_path):
            logging.warning(f"File not found: {file_path}")
            continue
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text = maybe_truncate_text(text, max_words)
            text = normalize_whitespace(text)
            chunks = divide_string_with_overlap(text=text, chunk_size=chunk_size, overlap=overlap)
            meta = {
                'title': row['title'],
                'url': row['result_link']
            }
            for chunk in chunks:
                valid_documents.append(Document(text=chunk.strip(), metadata=meta))

    logging.info("Count of chunks of text: %s", len(valid_documents))
    return valid_documents

def generate_unique_id(base_id):
    """Generates a unique identifier by appending a UUID to the base ID."""
    return f"{base_id}_{uuid.uuid4()}"

def main():
    parser = argparse.ArgumentParser(description="Process CSV and upsert data to Pinecone.")
    parser.add_argument('-csv', '--csv_file', required=True, help="Path to the CSV file.")
    parser.add_argument('-folder', '--file_folder', required=True, help="Folder containing the files referenced in the CSV.")
    parser.add_argument('-index', '--index_name', required=True, help="Name of the Pinecone index.")
    parser.add_argument('-rebuild', '--rebuild_index', action='store_true', help="Rebuild the index if specified.")
    parser.add_argument('-workers', '--num_workers', type=int, default=4, help="Number of workers for parallel processing.")
    parser.add_argument('-max_words', '--max_words_per_file', type=int, default=None, help="Maximum number of words per file.")
    parser.add_argument('-ns', '--namespace', required=True, help="Namespace for Pinecone index.")
    parser.add_argument('-cs', '--chunk_size', type=int, default=50, help="Chunk size for text division.")
    parser.add_argument('-ovlp', '--overlap', type=int, default=10, help="Overlap size for text division.")
    args = parser.parse_args()

    index_name = args.index_name

    active_indexes = [idx['name'] for idx in pc.list_indexes()]

    if args.rebuild_index:
        # Delete old vectors if rebuilding the index
        if index_name in active_indexes:
            index = pc.Index(index_name)
            delete_response = index.delete(delete_all=True, namespace=args.namespace)
            if len(delete_response) == 0:
                logging.info(f"Delete successful, Index: {index_name}, Namespace: {args.namespace}")
                print("Delete successful")

    documents = process_csv(args.csv_file, args.file_folder, max_words=args.max_words_per_file, chunk_size=args.chunk_size, overlap=args.overlap)

    if index_name not in active_indexes:
        pc.create_index(
            name=index_name,
            dimension=1536,
            metric='dotproduct',
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

    pineconeIndex = pc.Index(index_name)

    dense_embeds = embed_documents([doc.metadata['title'] + ' ' + doc.text for doc in documents], max_workers=args.num_workers)

    text_content = [doc.text for doc in documents]
    metadata = [doc.metadata for doc in documents]

    upserts = []
    for i, (dense, text, meta) in enumerate(zip(dense_embeds, text_content, metadata)):
        meta['body'] = text
        unique_id = generate_unique_id(i)
        upserts.append({
            'id': unique_id,
            'values': dense,
            'metadata': meta,
        })

    logging.info("Upserts length: %s", len(upserts))

    def divide_list(input_list, chunk_size=25):
        return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

    upserts_batch = divide_list(upserts, 25)
    for batch in tqdm(upserts_batch, desc="Upserting batches", total=len(upserts_batch)):
        pineconeIndex.upsert(vectors=batch, namespace=args.namespace)
    pineconeIndex.describe_index_stats()

    logging.info(f"Done building {index_name}!\n{len(documents)} documents upserted.")

if __name__ == "__main__":
    main()
