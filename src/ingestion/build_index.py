"""
=========================================
Module: Build FAISS Index
=========================================

Purpose:
    Executes the complete document
    ingestion pipeline.

Pipeline:

PDF Folder
     ↓
Document Loader
     ↓
Text Splitter
     ↓
Embeddings
     ↓
FAISS Index
"""

from pathlib import Path
import pickle

import faiss
import numpy as np

from config.settings import (
    KNOWLEDGE_PATH,
    VECTOR_DB_PATH,
    FAISS_INDEX_FILE,
    CHUNKS_FILE
)

from src.ingestion.document_loader import DocumentLoader
from src.ingestion.text_splitter import TextSplitter
from src.ingestion.embedder import Embedder


class BuildIndex:
    """
    Executes the complete ingestion pipeline
    and builds the FAISS vector database.

    By default it reads from the knowledge folder,
    but any folder path can be supplied.
    """

    def __init__(self, document_path=KNOWLEDGE_PATH):

        # Store the folder that contains documents
        self.document_path = Path(document_path)

        # Initialize pipeline
        self.loader = DocumentLoader(self.document_path)
        self.splitter = TextSplitter()
        self.embedder = Embedder()

    def build(self):

        print("\n========== DOCUMENT LOADER ==========\n")

        documents = self.loader.load_documents()

        print("\n========== TEXT SPLITTER ==========\n")

        chunks = self.splitter.split_documents(documents)

        print("\n========== EMBEDDINGS ==========\n")

        embeddings = self.embedder.embed_documents(chunks)

        embeddings = np.array(
            embeddings,
            dtype=np.float32
        )

        print("\n========== BUILDING FAISS ==========\n")

        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(dimension)

        index.add(embeddings)

        # -------------------------------------
        # Create vector database directory
        # -------------------------------------

        vector_store_path = Path(VECTOR_DB_PATH)

        vector_store_path.mkdir(
            parents=True,
            exist_ok=True
        )

        # -------------------------------------
        # Output files
        # -------------------------------------

        index_path = vector_store_path / FAISS_INDEX_FILE

        chunks_path = vector_store_path / CHUNKS_FILE

        # -------------------------------------
        # Save FAISS Index
        # -------------------------------------

        faiss.write_index(
            index,
            str(index_path)
        )

        # -------------------------------------
        # Save Chunks
        # -------------------------------------

        with open(chunks_path, "wb") as file:
            pickle.dump(chunks, file)

        print("\n✅ FAISS Index Saved Successfully.")

        print(f"\n📦 Total Vectors : {index.ntotal}")

        print(f"\n📂 Documents Folder : {self.document_path}")

        print(f"📁 FAISS Index : {index_path}")

        print(f"📁 Chunks File : {chunks_path}")

        return index