"""
=========================================
Test: Prompt Builder
=========================================
"""

from src.retrieval.retriever import Retriever
from src.chatbot.prompt_builder import PromptBuilder


def main():

    retriever = Retriever()

    prompt_builder = PromptBuilder()

    question = input("Ask a question: ")

    chunks = retriever.retrieve(question)

    prompt = prompt_builder.build_prompt(
        question,
        chunks
    )

    print("\n========== GENERATED PROMPT ==========\n")

    print(prompt)


if __name__ == "__main__":
    main()