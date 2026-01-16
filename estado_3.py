import streamlit as st

# Crear un input de texto
text = st.text_input(key="input_texto", label = "Introduzca un texto aquí")
# Ya no se puede modificar el valor del widget después de su creación

st.session_state.input_texto = "New Value"
# Generará una excepción StreamlitAPIException