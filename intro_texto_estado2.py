import streamlit as st
import datetime

# Inicializar si no existe
if 'mi_texto' not in st.session_state:
    st.session_state.mi_texto = ""

def manejar_cambio():
    print(f"Texto cambiado a: {st.session_state.mi_texto}")
    # Aquí puedes realizar otras operaciones con el nuevo valor

st.text_input("Introduce texto", 
             value=st.session_state.mi_texto,
             key="mi_texto",
             on_change=manejar_cambio)

st.write("Valor actual:", st.session_state.mi_texto)

# Imprimimos en pantalla el estado de sesión
st.json(st.session_state)