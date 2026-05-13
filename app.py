import streamlit as st

st.title("Mi primera aplicación en Python")

st.sidebar.title ("Parámetros")

st.write("Elaborado por Luz Garcia")

Sesion = st.sidebar.selectbox("seeccione una sesion,["Sesion 1","Sesion 2", "Sesion 3", "Sesion 4"])
