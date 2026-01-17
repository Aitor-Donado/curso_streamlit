import streamlit as st
from conversor import convertir_presion
import pandas as pd

# Título de la aplicación
st.title("Conversor de Presión")

# Input para el valor de presión
valor = st.number_input("Ingrese el valor de presión:", min_value=0.0, format="%.4f")

# Selectbox para la unidad de entrada
unidad = st.selectbox(
    "Seleccione la unidad de entrada:",
    ["atmósferas", "mm de mercurio", "milibares", "pascales"]
)

# Botón para realizar la conversión
if st.button("Convertir"):
    # Convertir la presión
    atmosferas, mm_de_mercurio, milibares, pascales = convertir_presion(valor, unidad)
    
    # Crear una tabla con los resultados
    resultados = {
        "Valor calculado": [atmosferas, mm_de_mercurio, milibares, pascales],
        "Unidad": ["atmósferas", "mm de mercurio", "milibares", "pascales"]
    }
    resultados_df = pd.DataFrame(resultados)
    # Mostrar la tabla
    resultados_df.set_index("Unidad", inplace=True)
    st.table(resultados_df)
