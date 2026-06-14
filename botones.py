import streamlit as st
import time

# Desencadenar acciones al pulsar el botón
boton = st.button("Pulsa", on_click = lambda: print("Pulsado"))

# Descargar un objeto
text_contents = '''Texto que se descargará'''
st.download_button('Descarga archivo de texto', text_contents, file_name='texto.txt')
st.download_button('Descarga este script', data = open(__file__, 'r').read(), file_name='botones.py')
# Descargar el pickle Ejemplos/Uso_modelo_entrenado/modelo_entrenado.pkl
st.download_button('Descarga el modelo entrenado', data = open("Ejemplos/Uso_modelo_entrenado/modelo_entrenado.pkl", 'rb').read(), file_name='model.pkl')

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