import streamlit as st

st.image("imagenes/arbol.png", caption = "Árbol de decisión", width = 650)
st.audio("imagenes/musica.mp3")
st.video("imagenes/sample.mp4")

# En el archivo main.py
import streamlit as st
# Vamos a ocultar la hamburguesa
# Podemos hacerlo con cualquier otra clase
st.markdown("""
<style>
.css-d1b1ld.edgvbvh6
{visibility: hidden;}
</style>
""", unsafe_allow_html = True)
