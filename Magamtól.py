import streamlit as st
st.write("Hatványozás 2-vel")

level = st.slider("2 hatványa", 0, 1000)
st.text('Selected: {}'.format(2**level))
