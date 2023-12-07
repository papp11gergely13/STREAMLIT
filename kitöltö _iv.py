import streamlit as st

st.header(".header: This is a header") 

name = st.text_input(".text_input: Enter Your name", "Type Here ...")
email = st.text_input(".text_input: Enter Your name", "Type Here ...")
csuszka = st.slider("2 hatványa", 0, 100)
status = st.radio(".radio: Select Gender: ", ('Male', 'Female'))
