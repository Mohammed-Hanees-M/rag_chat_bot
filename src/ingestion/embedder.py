"""
=========================================
Module: Embedder
=========================================

Purpose:
    Loads the embedding model only once
    and generates embeddings for both
    documents and user queries.
"""

from sentence_transformers import SentenceTransformer

from config.settings import EMBEDDING_MODEL


class Embedder:
    """
    Singleton class responsible for
    generating embeddings.
    """

    _model = None

    def __init__(self):

        if Embedder._model is None:

            print("\n🧠 Loading Embedding Model...")

            Embedder._model = SentenceTransformer(
                EMBEDDING_MODEL
            )

            print("✅ Embedding Model Loaded Successfully.\n")

    @property
    def model(self):
        return Embedder._model

    def embed_documents(self, chunks):
        """
        Generate embeddings for document chunks.
        """

        texts = [
            chunk.page_content
            for chunk in chunks
        ]

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )

        print(f"\n✅ Generated {len(embeddings)} embeddings.")

        return embeddings

    def embed_query(self, question):
        """
        Generate embedding for user query.
        """

        return self.model.encode(question)