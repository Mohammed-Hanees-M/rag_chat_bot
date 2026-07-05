# Retrieve relevant chunks
"""
=========================================
Module: Retriever
=========================================

Purpose:
    Loads the FAISS index and retrieves
    the most relevant document chunks.
"""

from pathlib import Path
import pickle

import faiss

from config.settings import (
    VECTOR_DB_PATH,
    FAISS_INDEX_FILE,
    CHUNKS_FILE,
    TOP_K_RESULTS
)

from src.ingestion.embedder import Embedder


class Retriever:

    def __init__(self):

        print("\nLoading Retriever...\n")

        self.embedder = Embedder()

        vector_path = Path(VECTOR_DB_PATH)

        self.index = faiss.read_index(
            str(vector_path / FAISS_INDEX_FILE)
        )

        with open(
            vector_path / CHUNKS_FILE,
            "rb"
        ) as file:

            self.chunks = pickle.load(file)

        print("Retriever Ready.\n")

    def retrieve(self, question):

        question_embedding = self.embedder.embed_query(question)

        question_embedding = question_embedding.reshape(1, -1)

        distances, indices = self.index.search(
            question_embedding,
            TOP_K_RESULTS
        )

        retrieved_chunks = []

        for idx in indices[0]:

            retrieved_chunks.append(
                self.chunks[idx]
            )

        return retrieved_chunks