"""
=========================================
Test: Upload Manager
=========================================
"""

from src.uploader.upload_manager import UploadManager
from src.uploader.knowledge_mode import KnowledgeMode


def main():

    manager = UploadManager()

    uploaded_files = [

        "uploads/Artificial_Intelligence.pdf"

    ]

    manager.process(
        uploaded_files,
        KnowledgeMode.REPLACE
    )


if __name__ == "__main__":

    main()