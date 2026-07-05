"""
=========================================
Test: Gemini
=========================================
"""

from src.chatbot.llm import GeminiLLM


def main():

    llm = GeminiLLM()

    question = input("Ask Gemini: ")

    answer = llm.generate_answer(question)

    print("\n========== GEMINI RESPONSE ==========\n")

    print(answer)


if __name__ == "__main__":
    main()