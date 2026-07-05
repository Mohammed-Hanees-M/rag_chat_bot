"""
=========================================
Status Card UI
=========================================

Displays the current application status.
"""

import streamlit as st


def render_status(
    documents_processed,
    mode,
    uploaded_files
):
    """
    Display the status panel.
    """

    st.subheader("📊 Status")

    # -----------------------------
    # Knowledge Base Status
    # -----------------------------

    if documents_processed:

        st.success("🟢 Knowledge Base Ready")

    else:

        st.warning("🟡 Waiting for Processing")

    st.write("")

    # -----------------------------
    # Current Mode
    # -----------------------------

    st.markdown("### ⚙️ Current Mode")

    if "Replace" in mode:

        st.info("Replace Knowledge Base")

    elif "Add" in mode:

        st.info("Add Documents")

    elif "Skip" in mode:

        st.info("Skip Duplicate Documents")

    elif "Update" in mode:

        st.info("Update Existing Documents")

    st.write("")

    # -----------------------------
    # Uploaded Files
    # -----------------------------

    st.markdown("### 📄 Uploaded Files")

    if uploaded_files:

        for file in uploaded_files:

            st.success(file.name)

    else:

        st.info("No files uploaded.")