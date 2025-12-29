import streamlit as st


def show_file_uploader():
    st.markdown(
        """
        <style>
        .stFileUploader  {
            position: fixed;
            bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.sidebar.file_uploader(
        "Upload a .txt file with numbers separated by spaces or commas:",
        type=["txt"],
        accept_multiple_files=False,
        label_visibility="collapsed"
    )
