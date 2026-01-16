import streamlit as st
import pandas as pd
import numpy as np

# Configuración de página
st.set_page_config(page_title="Demo: Sidebar & Tabs", layout="wide")

# 1. SIDEBAR - Es un namespace especial (st.sidebar, no st.side_bar())
with st.sidebar:
    st.title("⚙️ Panel de Control")
    st.divider()
    
    # Widgets en el sidebar
    nombre = st.text_input("¿Cómo te llamas?", "Alumno")
    color_favorito = st.selectbox(
        "Elige un color:",
        ["Azul", "Verde", "Rojo", "Morado"]
    )
    cantidad = st.slider("Nivel de entusiasmo", 1, 10, 5)
    
    # Mostrar datos del usuario
    st.divider()
    st.write(f"Hola **{nombre}**!")
    st.write(f"Color elegido: :{color_favorito.lower()}[{color_favorito}]")
    st.write(f"Nivel: {'⭐' * cantidad}")

# 2. CONTENIDO PRINCIPAL
st.title("📚 Demostración de Layout en Streamlit")
st.write(f"Bienvenido/a, **{nombre}**. Aquí puedes ver diferentes formas de organizar contenido.")

# 3. TABS - Dividir el contenido en pestañas
tab1, tab2, tab3 = st.tabs(["📈 Datos y Gráficos", "📊 Tabla Dinámica", "ℹ️ Información"])

with tab1:
    st.header("Análisis de Datos")
    
    # Usando columns dentro de un tab
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Gráfico de Líneas")
        # Datos aleatorios
        datos = pd.DataFrame({
            'x': range(1, 11),
            'y': np.random.randn(10).cumsum()
        })
        st.line_chart(datos.set_index('x'))
    
    with col2:
        st.subheader("Configuración")
        puntos = st.slider("Número de puntos", 5, 20, 10)
        st.write(f"Mostrando {puntos} puntos aleatorios")
        
        # Expander dentro de un column
        with st.expander("🔍 ¿Cómo se generan estos datos?"):
            st.write("""
            Los datos se crean usando NumPy:
            1. Se generan números aleatorios con distribución normal
            2. Se calcula la suma acumulativa
            3. Se muestran en un gráfico de líneas
            """)

with tab2:
    st.header("Tabla Interactiva")
    
    # Crear un DataFrame de ejemplo
    datos_tabla = pd.DataFrame({
        'Producto': ['Manzanas', 'Plátanos', 'Naranjas', 'Uvas', 'Fresas'],
        'Cantidad (kg)': np.random.randint(10, 100, 5),
        'Precio (€/kg)': np.round(np.random.uniform(1.5, 4.5, 5), 2),
        'Disponible': np.random.choice([True, False], 5)
    })
    
    # Añadir columna calculada
    datos_tabla['Valor Total (€)'] = datos_tabla['Cantidad (kg)'] * datos_tabla['Precio (€/kg)']
    
    st.dataframe(datos_tabla.style.highlight_max(axis=0), use_container_width=True)
    
    # Mostrar métricas resumen
    st.subheader("Resumen")
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    with metric_col1:
        st.metric("Productos Totales", len(datos_tabla))
    with metric_col2:
        st.metric("Cantidad Promedio", f"{datos_tabla['Cantidad (kg)'].mean():.1f} kg")
    with metric_col3:
        st.metric("Valor Total", f"{datos_tabla['Valor Total (€)'].sum():.2f} €")

with tab3:
    st.header("Recursos de Aprendizaje")
    
    # Contenedor para información
    with st.container():
        st.subheader("Elementos de Layout en Streamlit")
        
        # Lista de elementos con emojis
        elementos = [
            ("`st.sidebar`", "Barra lateral para controles y configuración"),
            ("`st.tabs()`", "Divide el contenido en pestañas independientes"),
            ("`st.columns()`", "Organiza contenido en columnas horizontales"),
            ("`st.expander()`", "Contenido plegable/desplegable"),
            ("`st.container()`", "Agrupa elementos para personalizar layout"),
            ("`st.empty()`", "Marcador de posición para contenido dinámico")
        ]
        
        for elemento, descripcion in elementos:
            st.markdown(f"- **{elemento}**: {descripcion}")
    
    # Usando st.empty() para contenido dinámico
    st.divider()
    st.subheader("Contenedor Vacío Dinámico")
    
    placeholder = st.empty()  # Contenedor vacío que llenaremos después
    
    if st.button("🎁 Haz clic para revelar", type="secondary"):
        with placeholder.container():  # Llenamos el placeholder
            st.success("¡Contenido dinámico cargado!")
            st.balloons()
            st.write("Este contenido apareció sin recargar toda la página.")
    else:
        with placeholder.container():
            st.info("Presiona el botón para ver contenido dinámico aquí.")

# 4. PIE DE PÁGINA
st.divider()
st.caption("Demo creada para la clase de Streamlit • Usa los controles en el sidebar para interactuar")