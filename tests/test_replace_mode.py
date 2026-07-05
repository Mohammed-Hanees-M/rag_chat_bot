"""
=========================================
Test: Replace Mode
=========================================
"""

from src.uploader.knowledge_manager import KnowledgeManager
from src.uploader.knowledge_mode import KnowledgeMode


def main():

    manager = KnowledgeManager()

    uploaded_files = [

        "uploads/Artificial_Intelligence.pdf"

    ]

    manager.process(
        uploaded_files,
        KnowledgeMode.REPLACE
    )


if __name__ == "__main__":

    main()