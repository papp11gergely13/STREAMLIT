import streamlit as st
st.write("2 hatványa")

level = st.slider(".slider: Select the level", 0, 16)
st.text('Selected: {}'.format(2**level))
