import streamlit as st
import pandas as pd
import numpy as np

# Utiliza columnas para colocar los inputs
# Title
st.title('App Streamlit Con Layouts y Containers')
col1, col2 = st.columns(2)

with col1:
    user_input = st.text_input("Enter some text")

with col2:
    number_input = st.number_input("Enter a number")

# Button in its own containerotón dentro de supropio contenedor
with st.container():
    if st.button('Púlsame'):
        st.write('¡Botón pulsado!')

# Dibujo de un gráfico en un "expander"
with st.expander("Ver el gráfico"):
    data = pd.DataFrame(np.random.randn(20, 2),
        columns=['A', 'B'])
    st.line_chart(data)

# Texto del pie de página dentro de un contenedor
with st.container():
    st.write("Pie de página con un texto.")