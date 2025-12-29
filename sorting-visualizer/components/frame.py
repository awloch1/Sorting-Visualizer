import plotly.graph_objects as go
import streamlit as st


def draw_frame(rand_list):
    fig = go.Figure(data=[
        go.Bar(x=list(range(len(rand_list))), y=rand_list, ),

    ], layout=dict(
        barcornerradius=5,
    ), )
    fig.update_layout(
        template="plotly_white",
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title="Index",
        yaxis_title="Value",
    )
    st.plotly_chart(fig, use_container_width=True)
