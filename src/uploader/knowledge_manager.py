"""
=========================================
Module: Knowledge Manager
=========================================

Purpose:
    Controls how uploaded documents
    affect the knowledge base.

Modes:

1. Replace Knowledge Base
2. Add Documents
3. Skip Duplicates
4. Update Existing
"""

from pathlib import Path

from config.settings import KNOWLEDGE_PATH

from src.uploader.file_manager import FileManager
from src.uploader.knowledge_mode import KnowledgeMode


class KnowledgeManager:
    """
    Handles updates to the knowledge base.
    """

    def __init__(self):

        self.file_manager = FileManager()

        self.knowledge_path = Path(KNOWLEDGE_PATH)

    # -------------------------------------------------
    # Main Dispatcher
    # -------------------------------------------------

    def process(self, uploaded_files, mode):
        """
        Routes the selected knowledge mode.
        """

        if mode == KnowledgeMode.REPLACE:

            self.replace(uploaded_files)

        elif mode == KnowledgeMode.ADD:

            self.add(uploaded_files)

        elif mode == KnowledgeMode.SKIP_DUPLICATES:

            self.skip_duplicates(uploaded_files)

        elif mode == KnowledgeMode.UPDATE_EXISTING:

            self.update_existing(uploaded_files)

        else:

            raise ValueError(f"Unsupported Mode: {mode}")

    # -------------------------------------------------
    # Mode 1
    # Replace Entire Knowledge Base
    # -------------------------------------------------

    def replace(self, uploaded_files):

        print("\n========== REPLACE MODE ==========\n")

        self._delete_documents()

        self._copy_documents(uploaded_files)

        print("\n✅ Knowledge Base Replaced Successfully.")

    # -------------------------------------------------
    # Mode 2
    # Add Documents
    # -------------------------------------------------

    def add(self, uploaded_files):

        print("\n========== ADD MODE ==========\n")

        print("🚧 Coming in next step...")

    # -------------------------------------------------
    # Mode 3
    # Skip Duplicate Files
    # -------------------------------------------------

    def skip_duplicates(self, uploaded_files):

        print("\n========== SKIP DUPLICATES MODE ==========\n")

        print("🚧 Coming in next step...")

    # -------------------------------------------------
    # Mode 4
    # Update Existing Files
    # -------------------------------------------------

    def update_existing(self, uploaded_files):

        print("\n========== UPDATE EXISTING MODE ==========\n")

        print("🚧 Coming in next step...")

    # -------------------------------------------------
    # Private Helper
    # Delete All Supported Documents
    # -------------------------------------------------

    def _delete_documents(self):

        for file in self.knowledge_path.iterdir():

            if file.is_file() and self.file_manager.is_supported(file):

                print(f"🗑 Removing : {file.name}")

                self.file_manager.delete_document(file)

    # -------------------------------------------------
    # Private Helper
    # Copy Uploaded Documents
    # -------------------------------------------------

    def _copy_documents(self, uploaded_files):

        for uploaded_file in uploaded_files:

            destination = self.knowledge_path / Path(uploaded_file).name

            self.file_manager.copy_document(
                uploaded_file,
                destination
            )

            print(f"✅ Added : {destination.name}")