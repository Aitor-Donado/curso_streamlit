import streamlit as st

# Inicializar el estado de sesión si no existe
if 'conteo' not in st.session_state:
    st.session_state.conteo = 0

# Función para incrementar el contador
def incrementa_contador():
    st.session_state.conteo += 1

# Botón que invcrementa el conteo
st.button('Incrementa el conteo', on_click=incrementa_contador)

# Texto que muestra el estado
st.write('Conteo: ', st.session_state.conteo)