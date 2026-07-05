"""
=========================================
Module: RAG Chatbot
=========================================

Purpose:
    Complete RAG pipeline:
    Question → Retrieval → Prompt → Gemini
"""

from src.retrieval.retriever import Retriever
from src.chatbot.prompt_builder import PromptBuilder
from src.chatbot.llm import GeminiLLM


class RAGChatbot:

    def __init__(self):

        print("\n🚀 Initializing RAG Chatbot...\n")

        self.retriever = Retriever()

        self.prompt_builder = PromptBuilder()

        self.llm = GeminiLLM()

        print("✅ RAG Chatbot Ready.\n")

    def ask(self, question):

        # Step 1: Retrieve relevant chunks
        retrieved_chunks = self.retriever.retrieve(question)

        # Step 2: Build prompt
        prompt = self.prompt_builder.build_prompt(
            question,
            retrieved_chunks
        )

        # Step 3: Generate response
        answer = self.llm.generate_response(prompt)

        return answer