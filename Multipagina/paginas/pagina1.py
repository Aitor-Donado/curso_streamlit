import streamlit as st

def mostrar():
    st.title("Página 1")
    st.write("Este es el contenido de la primera página.")
    st.text_input("Introduce algo:")
    st.button("Enviar")