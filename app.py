# app.py
import streamlit as st

st.title("Hello Streamlit!")
st.write("This is a simple Streamlit app.")
st.write("You can deploy it on Streamlit Cloud!")

# Add an input box and a button
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write(f"Hello, {name}!")
