import streamlit as st
import pandas as pd
import altair as alt
import folium
from folium.plugins import HeatMap, MarkerCluster
from streamlit_folium import st_folium

# --- Configuración de página ---
st.set_page_config(layout="wide")
st.title("Datos Accidentes Euskadi")

# --- 1. Cargar datos ---
@st.cache_data()
def cargar_datos():
    # Asegúrate de que esta ruta sea correcta en tu entorno
    df = pd.read_csv("Ejemplos/Ejemplo_accidentes/accidentes_2022.csv")
    df.drop(columns=["Unnamed: 0", "incidenceType", "sourceId", "autonomousRegion", "endDate", "incidenceName", "carRegistration", "pkEnd"], inplace=True, errors='ignore')
    df.rename(columns={"pkStart": "pk"}, inplace=True)
    return df

df = cargar_datos()

# --- 1. Inicializar estado de selecciones Y VERSIÓN DEL GRÁFICO ---
if 'filtro_causa' not in st.session_state:
    st.session_state.filtro_causa = None
if 'filtro_ciudad' not in st.session_state:
    st.session_state.filtro_ciudad = None
if 'chart_version' not in st.session_state:
    st.session_state.chart_version = 0  # Controla la "identidad" de los gráficos

# --- 3. Función para filtrar el DataFrame ---
def aplicar_filtros(df, causa_seleccionada, ciudad_seleccionada):
    df_filtrado = df.copy() # Importante: usar copy para evitar warnings
    if causa_seleccionada:
        df_filtrado = df_filtrado[df_filtrado['cause'] == causa_seleccionada]
    if ciudad_seleccionada:
        df_filtrado = df_filtrado[df_filtrado['cityTown'] == ciudad_seleccionada]
    return df_filtrado


# --- FUNCIÓN AUXILIAR PARA EXTRAER SELECCIÓN DE FORMA SEGURA ---
def extraer_seleccion(resultado_chart, nombre_param, campo):
    if not resultado_chart or 'selection' not in resultado_chart:
        return None
    selection = resultado_chart['selection']
    if nombre_param in selection and len(selection[nombre_param]) > 0:
        return selection[nombre_param][0].get(campo)
    return None

# --- 4. Interfaz: Columnas para los filtros ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Filtro por Causa")
    causa_counts = df['cause'].value_counts().reset_index()
    causa_counts.columns = ['cause', 'count']
    
    seleccion_causa = alt.selection_point(fields=['cause'], name='sel_causa')
    
    pie_causa = alt.Chart(causa_counts).mark_arc(innerRadius=30).encode(
        theta=alt.Theta(field="count", type="quantitative"),
        color=alt.Color(field="cause", type="nominal", scale=alt.Scale(scheme='category10')),
        tooltip=['cause', 'count']
    ).add_params(seleccion_causa).properties(height=300, title="Causas")
    
    resultado_causa = st.altair_chart(
        pie_causa, 
        on_select="rerun", 
        width='stretch', 
        # 👉 CLAVE DINÁMICA AQUI:
        key=f"pie_causa_v{st.session_state.chart_version}" 
    )
    # Ahora sí extraerá la causa correctamente
    causa_seleccionada = extraer_seleccion(resultado_causa, 'sel_causa', 'cause')
    st.session_state.filtro_causa = causa_seleccionada

with col2:
    st.subheader("Filtro por Ciudad")
    ciudad_counts = df['cityTown'].value_counts().head(10).reset_index()
    ciudad_counts.columns = ['cityTown', 'count']
    
    seleccion_ciudad = alt.selection_point(fields=['cityTown'], name='sel_ciudad')
    
    pie_ciudad = alt.Chart(ciudad_counts).mark_arc(innerRadius=30).encode(
        theta=alt.Theta(field="count", type="quantitative"),
        color=alt.Color(field="cityTown", type="nominal", scale=alt.Scale(scheme='category20')),
        tooltip=['cityTown', 'count']
    ).add_params(seleccion_ciudad).properties(height=300, title="Ciudades (top 10)")
    
    # 👉 CLAVE DINÁMICA AQUI:
    resultado_ciudad = st.altair_chart(
        pie_ciudad, 
        on_select="rerun", 
        width='stretch', 
        key=f"pie_ciudad_v{st.session_state.chart_version}" 
    )
    # Ahora sí extraerá la ciudad correctamente
    ciudad_seleccionada = extraer_seleccion(resultado_ciudad, 'sel_ciudad', 'cityTown')
    st.session_state.filtro_ciudad = ciudad_seleccionada

# --- Botón para limpiar filtros ---
if st.session_state.filtro_causa or st.session_state.filtro_ciudad:
    if st.button("🧹 Limpiar todos los filtros"):
        st.session_state.filtro_causa = None
        st.session_state.filtro_ciudad = None
        st.session_state.chart_version += 1  # 👉 INCREMENTAR VERSIÓN: Fuerza a Streamlit a olvidar la selección
        st.rerun()

# --- 5. Aplicar filtros al DataFrame principal ---
df_filtrado = aplicar_filtros(df, st.session_state.filtro_causa, st.session_state.filtro_ciudad)

# --- 6. Mostrar resultados ---
st.markdown("### 📊 Resultados Filtrados")
st.info(f"Mostrando {len(df_filtrado)} registros de un total de {len(df)}.")

st.subheader("Vista previa de los datos")
st.dataframe(df_filtrado.head(20), width='stretch') # Usar dataframe en lugar de table para mejor scroll

# --- 7. Mapas ---
st.markdown("### 🗺️ Visualización Geográfica")

# Verificar si hay coordenadas válidas
coordenadas = df_filtrado[['latitude', 'longitude']].dropna().values.tolist()

col_map1, col_map2 = st.columns(2)

with col_map1:
    st.subheader("Mapa de calor")
    mapa_heat = folium.Map(location=[43, -2.6], zoom_start=8)
    if coordenadas:
        HeatMap(coordenadas).add_to(mapa_heat)
        st_folium(mapa_heat, width="100%", height=400, key="mapa_heat")
    else:
        st.warning("No hay datos de ubicación para mostrar en el mapa de calor.")

with col_map2:
    st.subheader("Mapa con puntos aglomerables")
    mapa_cluster = folium.Map(location=[43, -2.6], zoom_start=9.5)
    if coordenadas:
        MarkerCluster(coordenadas).add_to(mapa_cluster)
        st_folium(mapa_cluster, width="100%", height=400, key="mapa_cluster")
    else:
        st.warning("No hay datos de ubicación para mostrar en el mapa de clústeres.")

# --- 8. Filtro adicional por variable categórica ---
st.markdown("---")
st.markdown("## Filtro adicional por variable categórica")
categoricas = df.columns[df.apply(lambda x: len(x.dropna().unique())) < 10].tolist()
categoricas = ["Ninguna"] + categoricas

seleccion_extra = st.selectbox("Elige variable categórica", options=categoricas)

if seleccion_extra != "Ninguna":
    opciones = sorted(df[seleccion_extra].dropna().unique().tolist())
    multi_select = st.multiselect(f"Elige categorías de '{seleccion_extra}'", options=opciones)
    
    if multi_select:
        df_filtrado = df_filtrado[df_filtrado[seleccion_extra].isin(multi_select)]
        st.success(f"Filtro aplicado: {len(df_filtrado)} registros restantes.")
        
        # Actualizar mapas dinámicamente si se aplica este filtro extra
        coordenadas_extra = df_filtrado[['latitude', 'longitude']].dropna().values.tolist()
        st.write("*(Los mapas de arriba se actualizarían si recargas o mueves los filtros principales, para una app en producción, envolverías los mapas en una función que tome `df_filtrado`)*")

# --- DEBUG (Opcional: Descomenta esto si sigue sin funcionar para ver qué devuelve Streamlit) ---
with st.expander("🔧 Depuración: Ver estado de selecciones"):
    st.write("Resultado Causa:", resultado_causa)
    st.write("Resultado Ciudad:", resultado_ciudad)
    st.write("Session State Causa:", st.session_state.filtro_causa)
    st.write("Session State Ciudad:", st.session_state.filtro_ciudad)
    st.json(st.session_state)