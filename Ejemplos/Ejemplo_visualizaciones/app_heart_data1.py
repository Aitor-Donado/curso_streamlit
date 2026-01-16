import streamlit as st
import pandas as pd

st.title("Datos heart_data.csv")

data = pd.read_csv("Ejemplos/Ejemplo_visualizaciones/heart_data.csv", index_col="id")

st.dataframe(data)