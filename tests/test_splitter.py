"""
=========================================
Test: Text Splitter
=========================================

Purpose:
    Tests the complete document loading
    and text chunking pipeline.
"""

from config.settings import KNOWLEDGE_PATH

from src.ingestion.document_loader import DocumentLoader
from src.ingestion.text_splitter import TextSplitter


def main():

    print("\n========== DOCUMENT LOADER ==========\n")

    loader = DocumentLoader(KNOWLEDGE_PATH)

    documents = loader.load_documents()

    print("\n========== TEXT SPLITTER ==========\n")

    splitter = TextSplitter()

    chunks = splitter.split_documents(documents)

    print("\n========== FIRST CHUNK ==========\n")

    print(chunks[0].page_content)

    print("\n===============================\n")

    print(f"Total Pages  : {len(documents)}")
    print(f"Total Chunks : {len(chunks)}")


if __name__ == "__main__":
    main()