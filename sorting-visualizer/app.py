import random

import streamlit as st

from components.file_uploader import show_file_uploader
from components.footer import show_footer_badge
from components.frame import draw_frames
from sorting_algorithms import ALGORITHMS, SortingAlgorithms

app_title = 'Sorting Visualizer'
st.set_page_config(page_title=app_title, page_icon=":el_salvador:", initial_sidebar_state="expanded")

# -- Sessions
if "data" not in st.session_state:
    st.session_state.data = None
if "rand_list" not in st.session_state:
    st.session_state.rand_list = None
if "last_n" not in st.session_state:
    st.session_state.last_n = None

# -- Sidebar
st.sidebar.title('Sorting Algorithms Visualizer')
algorithm_type = st.sidebar.selectbox(
    "Select Algorithm",
    ("-", *ALGORITHMS.keys())
)

n = st.sidebar.slider("N elements", 5, 70, 20, key="n")
fps = st.sidebar.slider("Speed ", 1, 30, 12)

if st.sidebar.button("🎲 Random Seed"):
    st.session_state.rand_list = random.sample(range(1, n + 1), n)
    st.session_state.last_n = n

show_file_uploader()

# -- Main page
if algorithm_type == "-":
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
            4️⃣ Use **⏸ Pause**, or **⟲ Reset** to control the animation.  

            💡 *Tip:*  
            Watch how compared elements are highlighted and how bars rearrange over time.
            """
        )
else:
    st.title(algorithm_type)
    data_source = st.session_state.get("data_source")

    if st.session_state.get("data_source") != "file":
        if st.session_state.rand_list is None or st.session_state.last_n != n:
            st.session_state.rand_list = random.sample(range(1, n + 1), n)
            st.session_state.last_n = n

    rand_list = st.session_state.rand_list[:]

    left, middle, right = st.columns(3)
    frames = []
    initial = rand_list[:]
    for f in SortingAlgorithms.sort(algorithm_type, rand_list):
        frames.append(f)
    draw_frames(initial, frames, fps=fps)

show_footer_badge("Aleksandra Włoch")
