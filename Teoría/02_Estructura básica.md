# 02 Estructura básica de una aplicación Streamlit

## Cómo crear un archivo de aplicación (`main.py`)

En este código vemos una muestra del repertorio de elementos que podemos incluir en una aplicación web se Streamlit.

El mismo código se encuentra en el archivo main.py del repositorio.

```python
# streamlit run main.py
import streamlit as st

st.title("Título de la web (H1)")
st.header("Encabezado (H2)")
st.subheader("Subtítulo (H3)")
st.write("## Encabezado (H2)")
st.text("Párrafo con texto normal")
st.markdown("**Texto** en formato *Markdown*")
# Barra de separación
st.caption("---")
st.divider()
# Fórmulas latex https://katex.org/
st.latex(r"e^2")
# Objeto json formateado en la pantalla
st.json({"Nombre": "Pedro", "Edad": 51})
codigo = """from math import pi"""
st.code(codigo, language = "python")

# Etiqueta de visualización de valores
st.metric(label = "Velocidad del viento", 
    value = "120m/s", 
    delta = "1.4m/s")

# Expander
with st.expander("📖 Contenido del expander"):
    st.markdown("""
    Los expander se utilizan cuando se quiere mostrar información adicional que 
    no es relevante para todos los usuarios o
    que se quiere ocultar para no saturar la pantalla.
    """)

# Visualización de un DataFrame
tabla = pd.read_csv("pequeña_tabla.csv")
st.table(tabla)
```

## Ejecución de una aplicación Streamlit (`streamlit run`)

Para arrancar el servidor web que ejecutará nuestra aplicación, ejecutamos en la terminal/powershell el siguiente comando. Tiene que estar activado el entorno virtual en el que hemos instalado Streamlit.

```bash
(venv) C:/> streamlit run main.py
```
