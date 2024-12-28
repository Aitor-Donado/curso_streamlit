import streamlit as st
import random
import pandas as pd
# Sample product data
productos = ['Teléf Móvil', 'Portátil', 'Auriculares', 'Cámara',
    'Smartwatch', 'Tablet', 'Cargador', 'Teclado', 'Ratón', 'Altavoces']

def generate_random_recommendations(prod_seleccionados, productos, num_recommendations=3):
    """Generador de recomendaciones aleatorias."""
    available_products = [p for p in productos if p not in prod_seleccionados]
    recomendaciones = random.sample(available_products, min(num_recommendations, len(available_products)))
    return recomendaciones

def crea_df_recomendaciones(recomendaciones):
    """Creamos un dataframe con probabilidades aleatorias."""
    # Generamos probabilidades aleatorias entre 50% y 99%
    probabilidades = [random.randint(50, 99) for _ in recomendaciones] 
    return pd.DataFrame({'Producto Recomendado': recomendaciones, 
                         'Probabilidad de compra': probabilidades})

# Layout
st.title('Recomendación de productos')
st.write('Selecciona al menos un producto para ver recomendaciones')
# Aquí elige los productos el usuario
prod_seleccionados = st.multiselect('Elige productos:', productos, default=None)

# Genera recomendaciones cuando se seleccione un producto
if prod_seleccionados:
    recomendaciones = generate_random_recommendations(prod_seleccionados, productos)
    # Crea y muestra el DataFrame con las recomendaciones
    df_recommendations = crea_df_recomendaciones(recomendaciones)

    st.write('Productos Recomendados:')

    config_probabilidad_compra = st.column_config.NumberColumn('Probabilidad de compra',
                                    help="Probabilidad de que quieras comprarlo **widget**",
                                    min_value=0,
                                    max_value=100,
                                    step=1,
                                    format="%d %%")

    st.dataframe(df_recommendations, 
                    column_config={'Probabilidad de compra': config_probabilidad_compra},
                    hide_index=True)
else:
    st.write('Selecciona al menos un producto para ver recomendaciones.')