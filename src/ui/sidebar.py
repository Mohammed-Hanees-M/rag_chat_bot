"""
=========================================
Sidebar UI
=========================================

Handles the complete sidebar interface.
"""

import streamlit as st


def render_sidebar():
    """
    Render the sidebar.

    Returns
    -------
    uploaded_files
    mode
    process_button
    """

    with st.sidebar:

        st.header("📂 Upload Documents")

        uploaded_files = st.file_uploader(
            "Select one or more PDF files",
            type=["pdf"],
            accept_multiple_files=True
        )

        st.divider()

        st.subheader("Knowledge Mode")

        mode = st.radio(

            "",

            [

                "Replace Knowledge Base",

                "Add Documents (Coming Soon)",

                "Skip Duplicate Documents (Coming Soon)",

                "Update Existing Documents (Coming Soon)"

            ]

        )

        st.divider()

        process_button = st.button(

            "🚀 Process Documents",

            use_container_width=True

        )

    return uploaded_files, mode, process_button