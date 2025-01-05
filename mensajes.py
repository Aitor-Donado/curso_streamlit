import streamlit as st
import time

# Título de la aplicación
st.title("Ejemplo de Mensajes en Streamlit")

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
    time.sleep(2)  # Espera 2 segundos para que el toast desaparezca
