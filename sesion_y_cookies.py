import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager


cookies = EncryptedCookieManager(
    prefix="preferencias/",
    password="clave_segura"
)

if not cookies.ready():
    st.stop()

# guardo la cookie en la sesión
if "usuario" not in st.session_state:
    st.session_state.usuario = cookies.get(
        "nombre",
        ""
    )

# Pone lo que estaba en la cookie como valor predeterminado en el text input
nombre_usuario = st.text_input(
    "Usuario",
    key="usuario"
)

# Guardo el nuevo valor en las cookies
if st.button("Guardar preferencia"):
    cookies["nombre"] = nombre_usuario
    cookies.save()

# Imprimimos en pantalla el estado de sesión
st.json(st.session_state)