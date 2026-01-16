import streamlit as st
# Forma incorrecta: Establecer el estado de un button después de su creación
st.session_state.my_button = True

if st.button("Click me", key = 'my_button'):
    st.write("Button was clicked!")