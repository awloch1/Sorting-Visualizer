import streamlit as st


def bottom_center_toast(text, success=True):
    color = "#2ecc71" if success else "#e74c3c"

    st.markdown(
        f"""
        <style>
        .custom-toast {{
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: {color};
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            font-weight: 600;
            z-index: 9999;
            box-shadow: 0 4px 14px rgba(0,0,0,.25);
            animation: fadeout 3s forwards;
        }}

        @keyframes fadeout {{
            0% {{ opacity: 1; }}
            70% {{ opacity: 1; }}
            100% {{ opacity: 0; }}
        }}
        </style>

        <div class="custom-toast">{text}</div>
        """,
        unsafe_allow_html=True
    )
