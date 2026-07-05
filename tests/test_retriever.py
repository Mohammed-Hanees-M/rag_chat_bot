# Retrieval tests
"""
=========================================
Test: Retriever
=========================================
"""

from src.retrieval.retriever import Retriever


def main():

    retriever = Retriever()

    question = input("\nAsk a question: ")

    results = retriever.retrieve(question)

    print("\n========== RETRIEVED CHUNKS ==========\n")

    for i, chunk in enumerate(results, start=1):

        print(f"\nChunk {i}")

        print("-" * 60)

        print(chunk.page_content)

        print()


if __name__ == "__main__":
    main()