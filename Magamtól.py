import streamlit as st
st.write("Hatványozás 2-vel")

csuszka = st.slider("2 hatványa", 0, 16)
st.text('Selected: {}'.format(2**csuszka))
