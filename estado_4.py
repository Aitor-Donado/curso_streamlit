import streamlit as st

# Forma incorrecta: Establecer el estado a través de la API de Session State y el parámetro value
st.session_state.text_input = "New Value"

text = st.text_input(key="text_input", 
                     label = "Enter text" , 
                     value = st.session_state.text_input)