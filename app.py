import streamlit as st


def say_hello():
    st.write("Hello, World!")


st.button("Say hello", on_click=say_hello)
