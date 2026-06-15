import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager


cookies = EncryptedCookieManager(
    prefix="preferencias/",
    password="clave_segura"
)

if not cookies.ready():
    st.stop()

if "usuario" not in st.session_state:
    st.session_state.usuario = cookies.get(
        "nombre",
        ""
    )


st.text_input(
    "Usuario",
    key="usuario"
)

# Imprimimos en pantalla el estado de sesión
st.json(st.session_state)