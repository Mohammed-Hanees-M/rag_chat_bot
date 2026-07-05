"""
=========================================
Module: Upload Manager
=========================================

Purpose:
    Coordinates the complete upload workflow.

Workflow:

Streamlit Upload
        ↓
Save to uploads/
        ↓
Knowledge Manager
        ↓
Build FAISS Index
"""

from pathlib import Path

from config.settings import UPLOAD_FOLDER

from src.ingestion.build_index import BuildIndex
from src.uploader.knowledge_manager import KnowledgeManager


class UploadManager:
    """
    Coordinates the upload workflow.
    """

    def __init__(self):

        self.knowledge_manager = KnowledgeManager()

        self.index_builder = BuildIndex()

        self.upload_folder = Path(UPLOAD_FOLDER)

        self.upload_folder.mkdir(
            parents=True,
            exist_ok=True
        )

    # -----------------------------------------
    # Save Uploaded Files
    # -----------------------------------------

    def save_uploaded_files(self, uploaded_files):

        saved_files = []

        for uploaded_file in uploaded_files:

            destination = self.upload_folder / uploaded_file.name

            with open(destination, "wb") as file:

                file.write(uploaded_file.getbuffer())

            saved_files.append(str(destination))

            print(f"📄 Saved: {destination.name}")

        return saved_files

    # -----------------------------------------
    # Process Upload
    # -----------------------------------------

    def process(self, uploaded_files, mode):

        print("\n========== UPLOAD MANAGER ==========\n")

        print("💾 Saving Uploaded Files...")

        saved_files = self.save_uploaded_files(uploaded_files)

        print("\n📄 Updating Knowledge Base...")

        self.knowledge_manager.process(
            saved_files,
            mode
        )

        print("\n🧠 Rebuilding FAISS Index...")

        self.index_builder.build()

        print("\n✅ Upload Completed Successfully.")