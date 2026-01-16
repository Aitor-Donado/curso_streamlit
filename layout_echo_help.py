import streamlit as st

# Setting the page config
st.set_page_config(page_title="Funciones echo y help",
    page_icon=":tada:",
    layout="wide")

# Displaying code and its output
with st.echo():
    # Este código se mostrará y se ejecutará.
    st.write("Esta línea de código se mostrará y después se ejecutará.")

# st.help renderiza la documentación de un objeto de Streamlit en la página de la aplicación.
st.help(st.sidebar)