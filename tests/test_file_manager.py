"""
=========================================
Test: File Manager
=========================================
"""

from config.settings import KNOWLEDGE_PATH
from src.uploader.file_manager import FileManager


def main():

    manager = FileManager()

    print("\n========== FILE MANAGER ==========\n")

    documents = manager.list_documents(KNOWLEDGE_PATH)

    print("Knowledge Base Documents:\n")

    for document in documents:

        print(f"✓ {document}")

    print("\nSupported Types:\n")

    for extension, name in manager.supported_types.items():

        print(f"{extension} -> {name}")


if __name__ == "__main__":
    main()