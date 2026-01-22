import hashlib

import streamlit as st
from components.toast import bottom_center_toast


def _parse_numbers(text: str):
    return [int(x) for x in text.replace(",", " ").split() if x]


def show_file_uploader():
    st.sidebar.markdown(
        """
        <style>
        [data-testid="stFileUploaderFile"] {
            display: none;
        }
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

    if uploaded_file is not None:
        data = uploaded_file.getvalue()
        file_key = hashlib.md5(data).hexdigest()

        if st.session_state.get("last_uploaded_key") != file_key:
            st.session_state.last_uploaded_key = file_key

            raw = data.decode("utf-8", errors="replace")
            try:
                num_list = _parse_numbers(raw)
                if not num_list:
                    raise ValueError("empty")

                st.session_state.rand_list = num_list
                st.session_state.data_source = "file"
                st.session_state.toast = ("✅ Your data was set!", "success")
            except Exception:
                st.session_state.toast = ("❌ Bad format. Use numbers separated by spaces or commas.", "error")

            st.rerun()

    toast = st.session_state.pop("toast", None)
    if toast:
        msg, kind = toast
        bottom_center_toast(
            msg,
            success=(kind == "success")
        )
