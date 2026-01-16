# 01 Introducción

## ¿Qué es Streamlit y para qué se utiliza?

**Streamlit** es una librería de Python de código abierto que permite crear aplicaciones web interactivas y visualizaciones de datos de manera sencilla y rápida. Fue diseñada específicamente para facilitar a los científicos de datos, analistas y desarrolladores la construcción de herramientas interactivas sin necesidad de tener conocimientos avanzados de desarrollo web o de manejar tecnologías como HTML, CSS o JavaScript.

### ¿Para qué se utiliza Streamlit?

1. **Visualización de datos**: Permite crear visualizaciones interactivas con gráficos, tablas, mapas y otros elementos de forma sencilla. Streamlit se integra perfectamente con bibliotecas populares de Python como **Matplotlib**, **Seaborn**, **Plotly** o **Altair** para generar gráficos y visualizaciones.
2. **Prototipos de aplicaciones de machine learning**: Streamlit es muy utilizado para crear interfaces gráficas donde los usuarios pueden interactuar con modelos de machine learning o algoritmos de inteligencia artificial. Por ejemplo, puedes permitir que los usuarios carguen datos, ajusten hiperparámetros y vean los resultados del modelo de forma inmediata.
3. **Dashboards y herramientas interactivas**: Los científicos de datos y analistas pueden construir rápidamente dashboards interactivos para explorar y presentar los datos de manera visual y dinámica. Streamlit ofrece una interfaz intuitiva para crear widgets como botones, sliders, menús desplegables, entre otros, sin complejidad adicional.
4. **Aplicaciones multipropósito**: Permite a los usuarios interactuar con aplicaciones que realizan múltiples tareas, como cargar archivos, procesar datos, mostrar gráficos y resultados, ejecutar cálculos o acceder a datos externos a través de APIs.
5. **Despliegue rápido de aplicaciones**: Streamlit facilita el despliegue de aplicaciones en la nube, lo que permite compartir los prototipos o productos finales con otras personas fácilmente, tanto en entornos locales como en la web a través de servicios como **Streamlit Cloud**, **Heroku** o **AWS**.

### Ventajas de usar Streamlit

Ventajas de usar Streamlit en comparación con otros frameworks de desarrollo web

- **Simplicidad**: Streamlit utiliza una API muy intuitiva y fácil de aprender. Basta con usar Python para desarrollar aplicaciones completas.
- **Rápido desarrollo**: Permite crear prototipos rápidos sin la necesidad de conocimientos avanzados de desarrollo web.
- **Interactividad**: Proporciona widgets interactivos como botones, selectores, sliders, etc., que pueden actualizar la interfaz en tiempo real.
- **Integración fácil**: Funciona bien con bibliotecas estándar de Python como NumPy, Pandas, Matplotlib, Seaborn, y herramientas de machine learning como Scikit-learn y TensorFlow.
- **Despliegue sencillo**: Es fácil de compartir aplicaciones mediante la web o a través de plataformas en la nube como **Streamlit Cloud**.

Es una herramienta ideal para aquellos que desean crear rápidamente aplicaciones web interactivas y dashboards para explorar y compartir datos o prototipos de modelos de machine learning, sin tener que preocuparse por la infraestructura o el diseño web tradicional.

### Instalación y configuración de Streamlit

```bash
pip install streamlit
```

### Documentación

- Streamlit official documentation: https://docs.streamlit.io/
- Streamlit official app gallery: https://streamlit.io/gallery
- Streamlit official component gallery: https://streamlit.io/components
- Streamlit official community boards: https://discuss.streamlit.io/
- Streamlit official GitHub repo: https://github.com/streamlit
- Streamlit and Snowflake official guide: https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit
- Jrieke GitHub repo for Streamlit projects: https://github.com/jrieke/best-of-streamlit
- MarcSkovMadsen GitHub repo for Streamlit projects: <https://github.com/MarcSkovMadsen/awesome-streamlit>

## La Magia de Streamlit

Como testimonio de la filosofía de Streamlit de ser una herramienta intuitiva y fácil de usar para los desarrolladores, Streamlit puede comprender y ejecutar de manera intuitiva comandos de Python para mostrar datos, crear diseños y agregar interactividad sin necesidad de realizar llamadas explícitas a las funciones de la API de Streamlit. Esto se denomina *Streamlit Magic*.

Con *Streamlit Magic*, no es necesario importar la biblioteca de Streamlit ni realizar llamadas explícitas a las API. Con solo escribir el código de Python como si estuviera escribiendo un script o un Jupyter Notebook, se mostrarán los resultados en la aplicación. Las cadenas de Python se representan automáticamente como texto en la aplicación Streamlit, y los marcos de datos, gráficos u otras visualizaciones se muestran directamente sin envolverlos en una función de Streamlit.

El siguiente fragmento de código es para demostrar la función *Streamlit Magic.* Si lo introducimos en un archivo con extensión `.py` se podrá ejecutar con `streamlit run archivo.py` y obtener una web en el navegador:

```python
# Archivo app_sin_import.py
import pandas as pd

"## Esto es un encabezado"
"Y esto es texto simple"

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

df
```

Esto sirve para hacer prototipos rápidos, pero no para tareas más complejas.
