# Tutorial de iniciación a streamlit

**Streamlit** es una librería de Python de código abierto que permite crear aplicaciones web interactivas y visualizaciones de datos de manera sencilla y rápida. Fue diseñada específicamente para facilitar a los científicos de datos, analistas y desarrolladores la construcción de herramientas interactivas sin necesidad de tener conocimientos avanzados de desarrollo web o de manejar tecnologías como HTML, CSS o JavaScript.

## ¿Para qué se utiliza Streamlit?

1. **Visualización de datos**: Permite crear visualizaciones interactivas con gráficos, tablas, mapas y otros elementos de forma sencilla. Streamlit se integra perfectamente con bibliotecas populares de Python como **Matplotlib**, **Seaborn**, **Plotly** o **Altair** para generar gráficos y visualizaciones.
2. **Prototipos de aplicaciones de machine learning**: Streamlit es muy utilizado para crear interfaces gráficas donde los usuarios pueden interactuar con modelos de machine learning o algoritmos de inteligencia artificial. Por ejemplo, puedes permitir que los usuarios carguen datos, ajusten hiperparámetros y vean los resultados del modelo de forma inmediata.
3. **Dashboards y herramientas interactivas**: Los científicos de datos y analistas pueden construir rápidamente dashboards interactivos para explorar y presentar los datos de manera visual y dinámica. Streamlit ofrece una interfaz intuitiva para crear widgets como botones, sliders, menús desplegables, entre otros, sin complejidad adicional.
4. **Aplicaciones multipropósito**: Permite a los usuarios interactuar con aplicaciones que realizan múltiples tareas, como cargar archivos, procesar datos, mostrar gráficos y resultados, ejecutar cálculos o acceder a datos externos a través de APIs.
5. **Despliegue rápido de aplicaciones**: Streamlit facilita el despliegue de aplicaciones en la nube, lo que permite compartir los prototipos o productos finales con otras personas fácilmente, tanto en entornos locales como en la web a través de servicios como **Streamlit Cloud**, **Heroku** o **AWS**.

## Ventajas de Streamlit

- **Simplicidad**: Streamlit utiliza una API muy intuitiva y fácil de aprender. Solo se necesita Python para desarrollar aplicaciones completas.
- **Rápido desarrollo**: Permite crear prototipos rápidos sin la necesidad de conocimientos avanzados de desarrollo web.
- **Interactividad**: Proporciona widgets interactivos como botones, selectores, sliders, etc., que pueden actualizar la interfaz en tiempo real.
- **Integración fácil**: Funciona bien con bibliotecas estándar de Python como NumPy, Pandas, Matplotlib, Seaborn, y herramientas de machine learning como Scikit-learn y TensorFlow.
- **Despliegue sencillo**: Es fácil de compartir aplicaciones mediante la web o a través de plataformas en la nube como **Streamlit Cloud**.

Es una herramienta ideal para aquellos que desean crear rápidamente aplicaciones web interactivas y dashboards para explorar y compartir datos o prototipos de modelos de machine learning, sin tener que preocuparse por la infraestructura o el diseño web tradicional.

- Instalación y configuración de Streamlit

```bash
    pip install streamlit
```

- Documentación: [Documentación Oficial]

## Este repositorio también requiere las siguientes librerías

```bash
    pip install pandas
    pip install matplotlib
    pip install folium
    pip install streamlit-folium
    pip install plotly
```

## Para comenzar el curso

En la carpeta Teoría se encuentran los archivos de teoría.
En la carpeta Ejemplos se encuentran los ejemplos de código que incluyen:

- Ejemplo de conversor de unidades de presión. (`streamlit run Ejemplos/Ejercicio_presiones/app_presiones.py`)
- Aplicación que permite visualizar datos de de un csv subido por el usuario (`streamlit run Ejemplos/Ejemplo_visualizaciones/app_heart_data_fin.py`)
- Ejemplo de uso de Streamlit con datos de accidentes en Euskadi. (`streamlit run Ejemplos/Ejemplo_accidentes/app_accidentes.py`)

En la carpeta Ejercicios se encuentran los ejercicios propuestos.

[Documentación Oficial]: https://docs.streamlit.io/get-started
