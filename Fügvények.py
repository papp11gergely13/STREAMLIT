import streamlit as st
import matplotlib.pyplot as px
from streamlit_plotly_events import plotly_events

# Writes a component similar to st.write()
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)

# Can write inside of things using with!
with st.expander('Plot'):
    fig = px.line(x=[1], y=[1])
    selected_points = plotly_events(fig)

# Select other Plotly events by specifying kwargs
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig, click_event=True, hover_event=True)
