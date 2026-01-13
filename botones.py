import streamlit as st
import time

# Desencadenar acciones al pulsar el botón
boton = st.button("Pulsa", on_click = lambda: print("Pulsado"))

# Descargar un objeto
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

# Enlace a página
st.link_button("Go to gallery",
"https://streamlit.io/gallery")

# Botones para mostrar los diferentes mensajes
if st.button("Mostrar Mensaje de Error"):
    st.error('Este es un mensaje de error')

if st.button("Mostrar Mensaje de Advertencia"):
    st.warning('Este es un mensaje de advertencia')

if st.button("Mostrar Mensaje Informativo"):
    st.info('Este es un mensaje informativo')

if st.button("Mostrar Mensaje de Éxito"):
    st.success('Este es un mensaje de éxito')

if st.button("Mostrar Excepción"):
    st.exception('Ha ocurrido una excepción')

if st.button("Mostrar Toast"):
    st.toast('Mensaje que aparece y desaparece')
    time.sleep(2) 