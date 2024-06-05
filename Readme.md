# Google Files: Pinecone and OpenAI Integration

This repository contains scripts for embedding text documents and querying a Pinecone index using OpenAI's embedding model. The scripts facilitate the processing of CSV files, embedding text data, and interacting with a Pinecone index.

## Prerequisites

Ensure you have the following installed:

- Python 3.7+
- Pip

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your Pinecone and OpenAI API keys:
    ```env
    PINECONE_API_KEY=<your-pinecone-api-key>
    OPENAI_API_KEY=<your-openai-api-key>
    OPENAI_EMBEDDING_MODEL=text-embedding-3-small
    ```

## Scripts

### Process CSV and Upsert Data to Pinecone

The `process_csv.py` script processes a CSV file, embeds the text data, and upserts it into a Pinecone index.

#### Usage
    ```bash
    python process_csv.py -csv <path_to_csv_file> -folder <path_to_file_folder> -index <index_name> -ns <namespace> [-rebuild] [-workers <num_workers>] [-max_words <max_words_per_file>] [-cs <chunk_size>] [-ovlp <overlap>]
    ```

#### Arguments

- `-csv`, `--csv_file`: Path to the CSV file (required).
- `-folder`, `--file_folder`: Folder containing the files referenced in the CSV (required).
- `-index`, `--index_name`: Name of the Pinecone index (required).
- `-ns`, `--namespace`: Namespace for the Pinecone index (required).
- `-rebuild`, `--rebuild_index`: Rebuild the index if specified.
- `-workers`, `--num_workers`: Number of workers for parallel processing (default: 4).
- `-max_words`, `--max_words_per_file`: Maximum number of words per file (default: None).
- `-cs`, `--chunk_size`: Chunk size for text division (default: 50).
- `-ovlp`, `--overlap`: Overlap size for text division (default: 10).

### Query Pinecone with a Text Input

The `query_pinecone.py` script queries the Pinecone index with a text input and retrieves the top results.

#### Usage
    ```bash
    python query_pinecone.py -query <query_text> -index <index_name> -top_k <top_k_results> -ns <namespace>
    ```

#### Arguments

- `-query`, `--query_text`: Text input for the query (required).
- `-index`, `--index_name`: Name of the Pinecone index (required).
- `-top_k`, `--top_k_results`: Number of top results to retrieve (default: 10).
- `-ns`, `--namespace`: Namespace for the Pinecone index (required).

## Logging

Both scripts log their operations to log files (`process_pinecone.log` and `query_pinecone.log`) in the root directory. The logs include information about the process flow, warnings, and errors.

## License

This project is licensed under the MIT License.
