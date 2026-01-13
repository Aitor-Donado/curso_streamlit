import streamlit as st

st.title("Título de la web (H1)")
st.header("Encabezado (H2)")
st.subheader("Subtítulo (H3)")
st.write("## Encabezado (H2)")
st.write("### Encabezado (H3)")
st.write("#### Encabezado (H4)")
st.write("##### Encabezado (H5)")
st.write("###### Encabezado (H6)")
st.text("Párrafo con texto normal")
st.markdown("**Texto** en formato *Markdown*")
# Barra de separación
st.caption("---")
# Fórmulas latex https://katex.org/
st.latex(r"e^2")
st.latex(r"""% \f is defined as 1f(#2) using the macro
\relax{x} = \int_{-\infty}^\infty
    \hat\xi\,e^{2 \pi i \xi x}
    \,d\xi""")
# Objeto json formateado en la pantalla
st.json({"Nombre": "Pedro", "Edad": 51})
codigo = """from math import pi"""
st.code(codigo, language = "python")
# Etiqueta de visualización de valores
st.metric(label = "Velocidad del viento", 
          value = "120m/s", delta = "1.4m/s")

import pandas as pd
# Visualización de un DataFrame
tabla = pd.read_csv("Empresas.csv")
tabla = tabla.drop("Unnamed: 0", axis=1)
st.table(tabla.head(10))