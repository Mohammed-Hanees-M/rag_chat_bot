"""
=========================================
Module: Text Splitter
=========================================

Purpose:
    Splits loaded documents into smaller
    overlapping chunks for efficient
    embedding and retrieval.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.settings import CHUNK_SIZE, CHUNK_OVERLAP


class TextSplitter:
    """
    Splits LangChain Document objects into
    smaller overlapping chunks.
    """

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

    def split_documents(self, documents):
        """
        Split documents into smaller chunks.

        Args:
            documents (list):
                List of LangChain Document objects.

        Returns:
            list:
                List of chunked Document objects.
        """

        chunks = self.splitter.split_documents(documents)

        print(f"\n✅ Total Chunks Created: {len(chunks)}")

        return chunks