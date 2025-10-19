import streamlit as st

from components.footer import show_footer_badge

app_title = 'Sorting Visualizer'
st.set_page_config(page_title=app_title, page_icon=":brain:", initial_sidebar_state="expanded")

# -- Sidebar
st.sidebar.title('Sorting Algorithms Visualizer')
algorithm_type = st.sidebar.selectbox("", ("", "Bubble Sort", "Quick Sort", "Merge Sort"))
n = st.sidebar.slider("N elements", 5, 300, 40)
fps = st.sidebar.slider("Speed ", 1, 30, 12)
st.sidebar.button("🎲 Random Seed")

# col1, col2, col3 = st.columns(3)
# with col1:
#     st.button("▶ Play")
# with col2:
#     st.button("⏸ Pause")
# with col3:
#     st.button("⟲ Reset")

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

# -- Main page
if not algorithm_type:
    st.title("🌀 Sorting Algorithms Visualizer")
    st.subheader("Learn how sorting algorithms work through interactive visualizations.")

    st.markdown("---")

    st.markdown(
        """
        This app lets you **see** how popular sorting algorithms organize data.
        Watch the process step-by-step and understand the logic behind each method.
        Choose an algorithm from the sidebar to get started.
        """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🧩 Algorithms")
        st.write("Visualize Bubble Sort, Quick Sort, Merge Sort — and more soon!")
    with col2:
        st.markdown("### ⚙️ Controls")
        st.write("Play, pause, step through, and adjust the speed in real time.")
    with col3:
        st.markdown("### 📊 Visualization")
        st.write("Color-coded bars make each comparison and swap clear and intuitive.")

    st.markdown("---")
    with st.expander("ℹ️ How to use this app", expanded=True):
        st.markdown(
            """
            **Instructions:**

            1️⃣ Select a **sorting algorithm** from the sidebar on the left.  
            2️⃣ Adjust the **number of elements**, **animation speed (FPS)**, and optional **random seed**.  
            3️⃣ Click **▶ Play** to start the visualization.  
            4️⃣ Use **⏸ Pause**, **⏭ Step**, or **⟲ Reset** to control the animation.  

            💡 *Tip:*  
            Watch how compared elements are highlighted and how bars rearrange over time.
            """
        )
else:
    st.title(algorithm_type)

show_footer_badge("Aleksandra Włoch")
