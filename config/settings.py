"""
=========================================
Project Configuration Settings
=========================================

This file contains all configurable values
used throughout the RAG Chatbot project.

Changing values here automatically affects
the entire project.
"""

from pathlib import Path

# =========================================
# Base Project Directory
# =========================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================
# Knowledge Base
# =========================================

# Permanent knowledge base
KNOWLEDGE_PATH = BASE_DIR / "knowledge"

# Temporary uploaded documents
UPLOAD_PATH = BASE_DIR / "uploads"


# =========================================
# Text Chunking
# =========================================

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200


# =========================================
# Embedding Model
# =========================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

EMBEDDING_DIMENSION = 384


# =========================================
# Vector Database
# =========================================

VECTOR_DB_PATH = BASE_DIR / "vector_store" / "faiss_index"

FAISS_INDEX_FILE = "faiss.index"

CHUNKS_FILE = "chunks.pkl"


# =========================================
# Gemini Configuration
# =========================================

GEMINI_MODEL = "gemini-2.5-flash"

LLM_MODEL = GEMINI_MODEL

TEMPERATURE = 0.3

MAX_OUTPUT_TOKENS = 1024


# =========================================
# Retrieval
# =========================================

TOP_K_RESULTS = 7


# =========================================
# Supported File Types
# =========================================

SUPPORTED_DOCUMENTS = {
    ".pdf": "PDF",

    # Future Support
    ".docx": "Word Document",
    ".txt": "Text File",
}

# =========================================
# Upload Folder
# =========================================

UPLOAD_FOLDER = "uploads"