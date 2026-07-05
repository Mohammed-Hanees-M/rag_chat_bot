"""
=========================================
Module: Prompt Builder
=========================================

Purpose:
    Loads the RAG prompt template and
    inserts the retrieved context and
    user question.
"""

from pathlib import Path


class PromptBuilder:

    def __init__(self, prompt_path="prompts/rag_prompt.txt"):

        self.prompt_path = Path(prompt_path)

    def build_prompt(self, question, retrieved_chunks):

        context = "\n\n".join(
            chunk.page_content
            for chunk in retrieved_chunks
        )

        with open(
            self.prompt_path,
            "r",
            encoding="utf-8"
        ) as file:

            template = file.read()

        prompt = template.replace(
            "{context}",
            context
        )

        prompt = prompt.replace(
            "{question}",
            question
        )

        return prompt