import streamlit as st


def show_footer_badge(author: str):
    """Displays a floating footer badge in the bottom-right corner."""
    st.markdown(
        f"""
        <style>
        .custom-badge {{
            background:  #b30000; 
            position: fixed;
            right: 20px;
            bottom: 20px;
            color: white;
            padding: 8px 14px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 600;
            box-shadow: 0 3px 10px rgba(0,0,0,0.3);
            z-index: 100;
            transition: all 0.3s ease;
        }}
        .custom-badge:hover {{
            transform: scale(1.05);
            box-shadow: 0 4px 14px rgba(0,0,0,0.4);
            cursor: default;
        }}
        </style>

        <div class="custom-badge"><b>{author}</b></div>
        """,
        unsafe_allow_html=True
    )
