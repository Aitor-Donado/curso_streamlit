import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager


cookies = EncryptedCookieManager(
    prefix="preferencias/",
    password="clave_segura"
)

if not cookies.ready():
    st.stop()

if "nombre" in cookies:
    nombre = cookies["nombre"]
else:
    nombre = ""


nombre_usuario = st.text_input(
    "Nombre",
    value=nombre
)

if st.button("Guardar preferencia"):
    cookies["nombre"] = nombre_usuario
    cookies.save()

    st.success("Preferencia guardada")

# Imprimimos en pantalla el estado de sesión
if "nombre" in cookies:
    st.json(st.session_state)