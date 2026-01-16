import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

st.title("Datos heart_data.csv")

data = pd.read_csv("Ejemplos/Ejemplo_visualizaciones/heart_data.csv", index_col="id")
del data["index"]
st.dataframe(data)

col1, col2 = st.columns(2)

# Gráfico 1: Gráfico de barras de colesterol

with col1:
    st.write("Categorías. Gráfico de barras:")
    categoricas = data.columns[data.apply(lambda x: len(x.unique()))<10]
    #st.write(categoricas)
    seleccion = st.selectbox("Elige variable categórica", options= categoricas)
    #st.write(seleccion)
    grafico = data[seleccion].value_counts().plot(kind="bar")
    st.pyplot(grafico.figure)  # Mostrar el gráfico en la primera columna

# Filtrar los datos para el segundo gráfico
data_filtrada = data[(data["ap_hi"] < 300) & (data["ap_hi"] > 50)]

# Gráfico 2: Boxplot de ap_hi por cardio
with col2:
    st.write("Boxplot de numéricas en función de categóricas:")

    # categoricas = data.columns[data.apply(lambda x: len(x.unique()))<4]

    numericas = data.select_dtypes("number").columns
    numericas_no_cat = numericas.difference(categoricas)

    seleccion_num = st.selectbox("Elige variable numérica", options= numericas_no_cat)
    seleccion_cat = st.selectbox("Elige variable categórica", options= categoricas, key="cat2")
    st.write(seleccion_num)
    st.write(seleccion_cat)
    
    grafico2 = data_filtrada.boxplot(column=seleccion_num, by=seleccion_cat, ax=None, fontsize=None, rot=90, grid=True)
    st.pyplot(grafico2.figure)  # Mostrar el gráfico en la segunda columna

# Crear el heatmap de correlación
st.write("Heatmap de correlación:")
f, ax = plt.subplots(figsize=(10, 8))
data_num = data.select_dtypes("number")
corr = data_num.corr()
sns.heatmap(corr, annot=True,
            mask=np.triu(np.ones_like(corr)),
            cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True,
            ax=ax)

# Mostrar el gráfico en Streamlit
st.pyplot(f)
