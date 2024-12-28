import streamlit as st
import random

if st.checkbox("Detener la aplicación"):
    st.write("Aplicación detenida.")
    st.stop()

st.write("Si marcas detener la app desaparece el contenido.")
if st.button("Rerun the app"):
    st.rerun()

# Display a random number
st.write(random.randint(1, 100))

with st.form(key='my_form'):
    text_input = st.text_input(label='Introduce texto')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f'Has introducido: {text_input}')