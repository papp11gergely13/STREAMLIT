import streamlit as st
st.write("2 hatványa")

level = st.slider("2 hatványa", 0, 16)
st.text('Selected: {}'.format(2**level))
