"""
=========================================
Chat UI
=========================================

Renders the chat interface.
"""

import streamlit as st


# =========================================
# Chat Input
# =========================================

def render_chat_input():
    """
    Display the chat input.

    Returns
    -------
    question : str
    """

    return st.chat_input(
        "Ask anything about the uploaded document..."
    )


# =========================================
# Conversation
# =========================================

def render_chat_history(chat_history):
    """
    Display the conversation history.
    """

    if not chat_history:

        st.info(
            """
👋 Welcome!

### How to use

1️⃣ Upload a PDF document.

2️⃣ Select **Replace Knowledge Base**

3️⃣ Click **🚀 Process Documents**

4️⃣ Ask any question about the document.

The chatbot answers **ONLY** from the uploaded document.
"""
        )

        return

    for chat in chat_history:

        with st.chat_message("user", avatar="👤"):

            st.markdown(chat["question"])

        with st.chat_message("assistant", avatar="🤖"):

            st.markdown(chat["answer"])


# =========================================
# Save Conversation
# =========================================

def add_message(question, answer):

    st.session_state.chat_history.append(

        {

            "question": question,

            "answer": answer

        }

    )