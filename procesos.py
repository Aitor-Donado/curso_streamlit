import streamlit as st
import time

# Título de la aplicación
st.title("Ejemplo de Widgets en Streamlit")

# Botón para mostrar una barra de progreso
if st.button("Mostrar Barra de Progreso"):
    progress_bar = st.progress(0)  # Inicializa la barra de progreso en 0%
    for i in range(100):
        time.sleep(0.05)  # Simula una tarea que toma tiempo
        progress_bar.progress(i + 1)  # Actualiza la barra de progreso
    st.success("¡Progreso completado!")

# Botón para mostrar un spinner de carga
if st.button("Mostrar Spinner de Carga"):
    with st.spinner("Procesando..."):
        time.sleep(3)  # Simula una tarea que toma tiempo
    st.success("¡Procesamiento completado!")

# Botón para mostrar un estado de operación
if st.button("Mostrar Estado de Operación"):
    with st.status("Tarea en progreso...", state="running") as status:
        time.sleep(2)  # Simula una tarea en progreso
        status.update(label="Tarea completada", state="complete")
    st.success("¡Estado actualizado!")

# Botón para mostrar globos de celebración
if st.button("Mostrar Globos de Celebración"):
    st.balloons()
    st.success("¡Celebremos este logro!")

# Botón para mostrar efecto de nieve
if st.button("Mostrar Efecto de Nieve"):
    st.snow()
    st.success("¡Es hora de festejar con nieve!")
