"""
=========================================
Test: Complete RAG Chatbot
=========================================
"""

from src.chatbot.rag_chatbot import RAGChatbot


def main():

    chatbot = RAGChatbot()

    print("\nType 'exit' to quit.\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            break

        answer = chatbot.ask(question)

        print("\nBot:\n")

        print(answer)

        print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":
    main()