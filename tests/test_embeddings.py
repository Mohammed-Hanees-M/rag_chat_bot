"""
=========================================
Test: Embedding Generation
=========================================
"""

from config.settings import KNOWLEDGE_PATH

from src.ingestion.document_loader import DocumentLoader
from src.ingestion.text_splitter import TextSplitter
from src.ingestion.embedder import Embedder


def main():

    print("\n========== DOCUMENT LOADER ==========\n")

    loader = DocumentLoader(KNOWLEDGE_PATH)
    documents = loader.load_documents()

    print("\n========== TEXT SPLITTER ==========\n")

    splitter = TextSplitter()
    chunks = splitter.split_documents(documents)

    print("\n========== EMBEDDING MODEL ==========\n")

    embedder = Embedder()

    embeddings = embedder.embed_documents(chunks)

    print("\n========== RESULTS ==========\n")

    print(f"Total Chunks      : {len(chunks)}")
    print(f"Total Embeddings  : {len(embeddings)}")
    print(f"Embedding Size    : {len(embeddings[0])}")

    print("\nFirst Embedding (First 10 Values):\n")

    print(embeddings[0][:10])


if __name__ == "__main__":
    main()