import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt


st.title("Datos heart_data.csv")

data = pd.read_csv("Ejemplos/Ejemplo_visualizaciones/heart_data.csv", index_col="id")
del data["index"]
st.dataframe(data)

col1, col2 = st.columns(2)

# Gráfico 1: Gráfico de barras de colesterol
with col1:
    st.write("Gráfico de barras de colesterol:")
    grafico = data['cholesterol'].value_counts().plot(kind="bar")
    st.pyplot(grafico.figure)  # Mostrar el gráfico en la primera columna

# Filtrar los datos para el segundo gráfico
data_filtrada = data[(data["ap_hi"] < 300) & (data["ap_hi"] > 50)]

# Gráfico 2: Boxplot de ap_hi por cardio
with col2:
    st.write("Boxplot de presión arterial (ap_hi) en función de (cardio):")
    grafico2 = data_filtrada.boxplot(column="ap_hi", by="cardio", ax=None, fontsize=None, rot=90, grid=True)
    st.pyplot(grafico2.figure)  # Mostrar el gráfico en la segunda columna



