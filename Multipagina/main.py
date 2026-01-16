import streamlit as st
from paginas import home, pagina1, pagina2

# Configuración de la aplicación

st.set_page_config(page_title="Mi Aplicación Multipágina", 
                   layout="wide")
# Barra lateral para la navegación

st.sidebar.title("Navegación")
pagina = st.sidebar.selectbox("Selecciona una página", ["Inicio", "Página 1", "Página 2"])

# Mostrar la página seleccionada
if pagina == "Inicio":
    home.mostrar()
elif pagina == "Página 1":
    pagina1.mostrar()
elif pagina == "Página 2":
    pagina2.mostrar()