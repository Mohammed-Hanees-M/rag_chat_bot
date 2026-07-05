"""
=========================================
Module: File Manager
=========================================

Purpose:
    Handles all document file operations.

Responsibilities:
    - Validate document type
    - List documents
    - Check duplicates

This module DOES NOT know anything about:
    - FAISS
    - Embeddings
    - Gemini
    - Streamlit
"""

from pathlib import Path

from config.settings import SUPPORTED_DOCUMENTS


class FileManager:
    """
    Handles file-related operations.
    """

    def __init__(self):

        self.supported_types = SUPPORTED_DOCUMENTS

    # -----------------------------------------
    # Check Supported File Type
    # -----------------------------------------

    def is_supported(self, file_path):

        extension = Path(file_path).suffix.lower()

        return extension in self.supported_types

    # -----------------------------------------
    # Get File Extension
    # -----------------------------------------

    def get_extension(self, file_path):

        return Path(file_path).suffix.lower()

    # -----------------------------------------
    # Get File Name
    # -----------------------------------------

    def get_filename(self, file_path):

        return Path(file_path).name

    # -----------------------------------------
    # List Documents
    # -----------------------------------------

    def list_documents(self, folder_path):

        folder = Path(folder_path)

        documents = []

        for file in folder.iterdir():

            if file.is_file():

                if self.is_supported(file):

                    documents.append(file.name)

        return sorted(documents)

    # -----------------------------------------
    # Check Duplicate
    # -----------------------------------------

    def document_exists(self, folder_path, filename):

        folder = Path(folder_path)

        return (folder / filename).exists()
    
    # -----------------------------------------
    # Copy Document
    # -----------------------------------------

    def copy_document(self, source, destination):

        from pathlib import Path
        import shutil

        source = Path(source)

        destination = Path(destination)

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.copy2(
            source,
            destination
        )

    # -----------------------------------------
    # Delete Document
    # -----------------------------------------

    def delete_document(self, file_path):

        file_path = Path(file_path)

        if file_path.exists():

            file_path.unlink()    