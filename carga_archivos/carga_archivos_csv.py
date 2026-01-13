# En el archivo carga_archivos_csv.py
import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Cargar y Analizar CSV")

# Widget para cargar el archivo CSV
uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

# Verificar si se ha cargado un archivo
if uploaded_file is not None:
    # Leer el archivo CSV con pandas
    df = pd.read_csv(uploaded_file)

    # Mostrar el DataFrame cargado
    st.write("### Vista previa del DataFrame:")
    st.dataframe(df)  # Muestra las primeras filas del DataFrame

    # Mostrar el resumen estadístico usando df.describe()
    st.write("### Resumen estadístico:")
    st.write(df.describe())
else:
    st.info("Por favor, sube un archivo CSV para comenzar.")
