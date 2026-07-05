"""
=========================================
Test: Document Loader
=========================================

Purpose:
    Tests whether PDF documents are
    successfully loaded from the
    knowledge base.
"""

from config.settings import KNOWLEDGE_PATH

from src.ingestion.document_loader import DocumentLoader


def main():

    print("\n========== DOCUMENT LOADER ==========\n")

    loader = DocumentLoader(KNOWLEDGE_PATH)

    documents = loader.load_documents()

    print("\n========== FIRST PAGE ==========\n")

    print(documents[0].page_content[:1000])

    print("\n===============================\n")

    print(f"Total Pages Loaded : {len(documents)}")


if __name__ == "__main__":
    main()