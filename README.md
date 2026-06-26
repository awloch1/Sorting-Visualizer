# Sorting Visualizer

An interactive web application for visualizing sorting algorithms step by step.

The project was built with Python and Streamlit. It allows users to generate random data, upload custom input, choose a sorting algorithm, and observe how the algorithm changes the order of elements during execution.

## Overview

Sorting Visualizer is an educational project created to better understand how sorting algorithms work internally.

Instead of only showing the final sorted result, the application displays each intermediate step of the algorithm. This makes it easier to observe comparisons, swaps, pivot selection, and the overall sorting process.

## Features

- Interactive sorting visualization
- Random array generation
- Custom input upload from `.txt` files
- Adjustable number of elements
- Adjustable animation speed
- Play, pause, and replay controls
- Highlighting of currently compared or moved elements
- Clean visual interface built with Streamlit and a custom HTML/CSS/JavaScript component

## Implemented Algorithms

The application currently supports the following sorting algorithms:

- **Bubble Sort**
- **Selection Sort**
- **Insertion Sort**
- **Quick Sort**

## How It Works

The sorting algorithms generate a sequence of animation frames.  
Each frame represents one step of the sorting process, including the current order of elements and highlighted positions.

The visualization component then renders these frames as animated bars, allowing the user to follow the algorithm step by step.

## Project Structure

```text
Sorting-Visualizer/
├── sorting-visualizer/
│   ├── app.py
│   ├── sorting_algorithms.py
│   └── components/
│       ├── file_uploader.py
│       ├── footer.py
│       ├── frame.py
│       ├── toast.py
│       └── bar-component/
│           ├── bar-component.html
│           ├── bar-component.css
│           └── bar-component.js
├── requirements.txt
└── README.md
