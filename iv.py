import streamlit as st

st.header(".header: This is a header") 

name = st.text_input("Enter Your name", "Type Here ...")
email = st.text_input("Enter Your email", "Type Here ...")
csuszka = st.slider("Életkorod ", 0, 100)
status = st.radio(".radio: Select Gender: ", ('Male', 'Female'))

list = [name,email,csuszka,status]
if(st.button("submit")):
	st.text(list)
