import streamlit as st
import pandas as pd
data_df = pd.DataFrame(
    {"widgets": ["selectbox", 
                "st.number_input", 
                "st.text_area", 
                "st.button"],
    "widgets_func": ["Let's you select a value ", 
                     "Let's you input a number", 
                     "Let's you input text",
                     "Let's you click submission"],
    "widget_rank": [9, 950, 3, 1],
    "favorite": [True, False, False, True],
    "category": [
        "Data Exploration",
        "Data Visualization",
        "LLM",
        "Data Exploration"],
    })

# En esta columna se valida el texto
columna_texto = st.column_config.TextColumn("Widgets de Streamlit", 
                    help="Comandos **widget** de streamlit",
                    max_chars=50,
                    validate="^st\\.[a-z_]+$")

# En esta columna se puede meter cualquier cosa
columna = st.column_config.Column("Qué hacen",
            help="Función **widget** de streamlit",
            width="medium",
            required=True)

columna_numero = st.column_config.NumberColumn("Ranking", 
                    help="Ranking del **widget**",
                    min_value=0,
                    max_value=1000,
                    step=1,
                    format="%d")

columna_checkbox = st.column_config.CheckboxColumn("Tu favorito",
                        help="Elige tus favoritos",
                        default=False)

opciones = ["Data_Exploration", "Data_Visualization", "LLM"]
columna_selectbox = st.column_config.SelectboxColumn("Categoría del widget",
                        help="Categoría del widget",
                        width="medium",
                        options=opciones)

configuracion_columnas = {"widgets": columna_texto,
        "widgets_func": columna,
        "widget_rank": columna_numero,
        "favorite": columna_checkbox,
        "category": columna_selectbox}

st.data_editor(data_df,
    column_config=configuracion_columnas,
    hide_index=True)
