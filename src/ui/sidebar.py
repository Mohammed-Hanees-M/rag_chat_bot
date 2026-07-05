"""
=========================================
Toolbar UI
=========================================

Handles the horizontal toolbar interface.
"""

import streamlit as st


def render_toolbar():
    """
    Render the horizontal toolbar with 5 cards.

    Returns
    -------
    uploaded_files
    mode
    process_button
    """

    # Create 5 columns for the toolbar cards
    col1, col2, col3, col4, col5 = st.columns(5)

    # =========================================
    # CARD 1: Upload Documents
    # =========================================

    with col1:
        st.markdown("### 📂 Upload")
        uploaded_files = st.file_uploader(
            "Select PDF files",
            type=["pdf"],
            accept_multiple_files=True,
            label_visibility="collapsed"
        )

    # =========================================
    # CARD 2: Knowledge Mode
    # =========================================

    with col2:
        st.markdown("### ⚙ Mode")
        mode = st.radio(
            "Knowledge Mode",
            [
                "Replace Knowledge Base",
                "Add Documents (Coming Soon)",
                "Skip Duplicate Documents (Coming Soon)",
                "Update Existing Documents (Coming Soon)"
            ],
            label_visibility="collapsed",
            index=0
        )

    # =========================================
    # CARD 3: Current File
    # =========================================

    with col3:
        st.markdown("### 📄 File")
        if not uploaded_files:
            st.write("No file selected")
        elif len(uploaded_files) == 1:
            st.write(uploaded_files[0].name)
        else:
            st.write(f"{len(uploaded_files)} files")

    # =========================================
    # CARD 4: Process Documents
    # =========================================

    with col4:
        st.markdown("### 🚀 Process")
        process_button = st.button(
            "Process",
            use_container_width=True,
            key="process_btn"
        )

    # =========================================
    # CARD 5: Status
    # =========================================

    with col5:
        st.markdown("### 🟢 Status")
        
        if "documents_processed" in st.session_state:
            if st.session_state.documents_processed:
                st.success("Ready")
            else:
                st.warning("Waiting")
        else:
            st.warning("Waiting")

    return uploaded_files, mode, process_button


def render_sidebar():
    """
    Deprecated: Use render_toolbar() instead.
    Kept for backward compatibility.

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