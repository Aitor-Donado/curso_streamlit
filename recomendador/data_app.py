import streamlit as st
from recommend_app import recommend_main
from top_products_app import top_products_main

# Set page configuration
st.set_page_config(page_title="Recomendador de productos", 
                   page_icon="..",
                   layout="wide",
                   initial_sidebar_state="expanded")

texto_web = """
    > ¿Qué hace esta aplicación?
    * Esta aplicación ayuda a recomendar productos en función de los productos seleccionados por el usuario.
    * La aplicación también muestra los productos más populares de cada categoría.
    > ¿Cómo se usa?
    * Seleccione los productos del menú desplegable; también puede seleccionar varios productos.
    * El resultado se mostrará con los productos más recomendados con mayor probabilidad de compra.
    """

def intro():
    st.title('Product Recommender')
    st.markdown("---")
    st.markdown(texto_web)

# Barra lateral para que el usuario introduzca datos
with st.sidebar:
    st.write("Esta es una aplicación de demostración. Un ejercicio práctico para crear una aplicación de recomendación de productos.")

if __name__ == "__main__":
    # Pestañas de la página principal
    tab1, tab2, tab3 = st.tabs(["Intro", "Recomendador de productos", "Productos Top"])
    with tab1:
        intro()
    with tab2:
        recommend_main()
    with tab3:
        top_products_main()