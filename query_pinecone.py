import os
import argparse
import logging
from pinecone import Pinecone
from openai import OpenAI
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Configure the logging system
logging.basicConfig(filename='query_pinecone.log',  # Log file path
                    filemode='w',  # 'a' for append, 'w' for overwrite
                    format='%(asctime)s - %(levelname)s - %(message)s',  # Format of log messages
                    level=logging.INFO)  # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# Initialize Pinecone
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

# Initialize OpenAI
oai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

EMBEDDING_MODEL = os.getenv('OPENAI_EMBEDDING_MODEL', "text-embedding-3-small")

def embed_query(query: str, model=EMBEDDING_MODEL):
    """Embeds a query using the specified model."""
    embedding = oai.embeddings.create(input=[query], model=model).data[0].embedding
    return embedding

def query_pinecone(query: str, index_name: str, namespace: str, top_k: int = 10):
    """Queries the Pinecone index with the provided query."""
    # Embed the query
    dense_embedding = embed_query(query)

    # Initialize the index
    index = pc.Index(index_name)
    
    # Perform the query
    response = index.query(
        vector=[dense_embedding],
        top_k=top_k,
        include_metadata=True,
        namespace=namespace
    )
    
    return response

def main():
    parser = argparse.ArgumentParser(description="Query Pinecone with a text input.")
    parser.add_argument('-query', '--query_text', required=True, help="Text input for the query.")
    parser.add_argument('-index', '--index_name', required=True, help="Name of the Pinecone index.")
    parser.add_argument('-top_k', '--top_k_results', type=int, default=10, help="Number of top results to retrieve.")
    parser.add_argument('-ns', '--namespace', required=True, help="Namespace for Pinecone index.")
    
    args = parser.parse_args()

    query_text = args.query_text
    index_name = args.index_name
    top_k = args.top_k_results
    namespace = args.namespace

    response = query_pinecone(query_text, index_name, namespace, top_k)

    print("Query results:")
    for match in response['matches']:
        print(f"Score: {match['score']}")
        print(f"Title: {match['metadata']['title']}")
        print(f"URL: {match['metadata']['url']}")
        print(f"Text: {match['metadata']['body']}")
        print("-" * 80)

    logging.info("Query results: %s", response)

if __name__ == "__main__":
    main()
