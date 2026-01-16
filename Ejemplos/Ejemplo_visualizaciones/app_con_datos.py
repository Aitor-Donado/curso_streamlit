import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

def grafico_columna_categorica(data):
    st.write("Categorías. Gráfico de barras:")
    categoricas = data.columns[data.apply(lambda x: len(x.unique()))<4]
    #st.write(categoricas)
    seleccion = st.selectbox("Elige variable categórica", options= categoricas)
    #st.write(seleccion)
    if seleccion:
        grafico = data[seleccion].value_counts().plot(kind="bar")
        st.pyplot(grafico.figure)  # Mostrar el gráfico en la primera columna

def grafico_boxplot(data):
    st.write("Boxplot de numéricas en función de categóricas:")

    categoricas = data.columns[data.apply(lambda x: len(x.unique()))<4]

    numericas = data.select_dtypes("number").columns
    numericas_no_cat = numericas.difference(categoricas)

    seleccion_num = st.selectbox("Elige variable numérica", options= numericas_no_cat)
    seleccion_cat = st.selectbox("Elige variable categórica", options= categoricas, key="cat2")
    if seleccion_num and seleccion_cat:
        st.write(seleccion_num)
        st.write(seleccion_cat)
        
        grafico2 = data.boxplot(column=seleccion_num, by=seleccion_cat, ax=None, fontsize=None, rot=90, grid=True)
        st.pyplot(grafico2.figure)  # Mostrar el gráfico en la segunda columna

def grafico_correlacion(data):
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

def aplicacion_con_uploaded_file(uploaded_file):
    # Leer el archivo CSV con pandas
    data = pd.read_csv(uploaded_file)
    col1, col2 = st.columns(2)

    # Gráfico 1: Gráfico de barras de colesterol

    with col1:
        grafico_columna_categorica(data)

    # Gráfico 2: Boxplot de ap_hi por cardio
    with col2:
        grafico_boxplot(data)

    # Crear el heatmap de correlación
    with st.expander("Ver gráfico de correlación"):
        grafico_correlacion(data)
