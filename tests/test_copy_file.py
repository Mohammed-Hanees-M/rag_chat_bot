"""
=========================================
Test: Copy Document
=========================================
"""

from pathlib import Path

from config.settings import KNOWLEDGE_PATH
from src.uploader.file_manager import FileManager


def main():

    manager = FileManager()

    source = Path("uploads") / "Artificial_Intelligence.pdf"

    destination = Path(KNOWLEDGE_PATH) / "Artificial_Intelligence_Copy.pdf"

    manager.copy_document(
        source,
        destination
    )

    print("\n✅ File Copied Successfully.")

    print(destination)


if __name__ == "__main__":
    main()