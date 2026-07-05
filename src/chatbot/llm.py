"""
=========================================
Module: Gemini LLM
=========================================

Purpose:
    Uses Gemini as the primary LLM.
    Automatically falls back to Groq if
    Gemini fails (quota, rate limit, etc.).
"""

import os

from dotenv import load_dotenv
from google import genai

from config.settings import (
    LLM_MODEL,
    TEMPERATURE,
    MAX_OUTPUT_TOKENS,
)

from src.chatbot.groq_llm import GroqLLM


class GeminiLLM:
    """
    Gemini wrapper with automatic Groq fallback.
    """

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY not found in .env file."
            )

        self.client = genai.Client(
            api_key=api_key
        )

        # Initialize Groq once
        self.groq = GroqLLM()

        print("\n🤖 Gemini Client Loaded Successfully.")
        print("⚡ Groq Fallback Ready.\n")

    def generate_response(self, prompt):

        try:

            response = self.client.models.generate_content(
                model=LLM_MODEL,
                contents=prompt,
                config={
                    "temperature": TEMPERATURE,
                    "max_output_tokens": MAX_OUTPUT_TOKENS,
                },
            )

            return response.text.strip()

        except Exception as error:

            print("\n⚠ Gemini failed.")
            print(error)

            print("\n🔄 Switching to Groq...\n")

            return self.groq.generate_response(prompt)