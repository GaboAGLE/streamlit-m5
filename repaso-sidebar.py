import streamlit as st

st.title("Mi primera app")

sidebar = st.sidebar

sidebar.title("titulo barra lateral.")
sidebar.write("Aqui van los elementos de entrada")

st.header("info")
sidebar.header("header en el sidebar")