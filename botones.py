import streamlit as st

# Desencadenar acciones al pulsar el botón
boton = st.button("Pulsa", on_click = lambda: print("Pulsado"))

# Descargar un objeto
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

# Enlace a página
st.link_button("Go to gallery",
"https://streamlit.io/gallery")

