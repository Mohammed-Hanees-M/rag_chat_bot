"""
=========================================
RAG Document Chatbot
Main Streamlit Application
=========================================
"""

import streamlit as st

from src.chatbot.rag_chatbot import RAGChatbot
from src.uploader.upload_manager import UploadManager
from src.uploader.knowledge_mode import KnowledgeMode

from src.ui.styles import load_css
from src.ui.sidebar import render_sidebar
from src.ui.status_card import render_status
from src.ui.chat import (
    render_chat_input,
    render_chat_history,
    add_message
)


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="RAG Document Chatbot",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# Load Custom CSS
# ==========================================

load_css()


# ==========================================
# Session State
# ==========================================

if "chatbot" not in st.session_state:
    st.session_state.chatbot = None

if "documents_processed" not in st.session_state:
    st.session_state.documents_processed = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ==========================================
# Header
# ==========================================

st.title("📚 RAG Document Chatbot")

st.caption(
    "Upload a document and ask questions using Retrieval-Augmented Generation (RAG)."
)

st.divider()


# ==========================================
# Sidebar
# ==========================================

uploaded_files, mode, process_button = render_sidebar()


# ==========================================
# Layout
# ==========================================

chat_col, status_col = st.columns([3, 1])


# ==========================================
# Status Panel
# ==========================================

with status_col:

    render_status(
        st.session_state.documents_processed,
        mode,
        uploaded_files
    )


# ==========================================
# Upload Processing
# ==========================================

if process_button:

    if not uploaded_files:

        st.error(
            "Please upload at least one PDF document."
        )

    elif mode != "Replace Knowledge Base":

        st.info(
            """
🚧 This feature is coming soon.

Currently only

• Replace Knowledge Base

is implemented.
"""
        )

    else:

        try:

            with st.spinner("📚 Processing Documents..."):

                uploader = UploadManager()

                uploader.process(
                    uploaded_files,
                    KnowledgeMode.REPLACE
                )

                st.session_state.chatbot = RAGChatbot()

                st.session_state.documents_processed = True

            st.success(
                "✅ Knowledge Base Updated Successfully."
            )

        except Exception as error:

            st.error(error)


# ==========================================
# Chat
# ==========================================

with chat_col:

    render_chat_history(
        st.session_state.chat_history
    )

    question = render_chat_input()

    if question:

        if not st.session_state.documents_processed:

            st.warning(
                "Please process your document first."
            )

        else:

            try:

                with st.spinner("🤖 Thinking..."):

                    answer = st.session_state.chatbot.ask(
                        question
                    )

                add_message(
                    question,
                    answer
                )

                st.rerun()

            except Exception as error:

                st.error(error)