"""
=========================================
Module: Groq LLM
=========================================

Purpose:
    Connects to Groq API.
"""

import os

from dotenv import load_dotenv
from groq import Groq


class GroqLLM:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found in .env"
            )

        self.client = Groq(
            api_key=api_key
        )

        print("\n⚡ Groq Client Loaded Successfully.\n")

    def generate_response(self, prompt):

        response = self.client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3,

            max_tokens=1024

        )

        return response.choices[0].message.content