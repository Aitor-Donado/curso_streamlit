import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

# Función para cargar los datos en caché
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Cargar categorías de productos
data_products = load_data('data/products.csv')

def genera_recomendaciones(selected_products, product_data, num_recommendations=3):
    """
    Genera recomendaciones aleatorias a partir de productos disponibles.
    """
    available_products = product_data[~product_data['Product'].isin(selected_products)]
    recommendations = available_products.sample(n=min(num_recommendations, len(available_products)))
    return recommendations

def convierte_a_df_recomendaciones(recommendations):
    """
    Añade una columna con la probabilidad de compra a las recomendaciones.
    """
    recommendations['Probabilidad de Compra'] = [random.randint(50, 99) for _ in range(len(recommendations))]
    return recommendations[['Product', 'Probabilidad de Compra']]

def grafica_prob_de_compra(df_recommendations):
    """
    Genera un gráfico horizontal de barras mostrando la probabilidad de compra.
    """
    fig, ax = plt.subplots(figsize=(6, 4))
    df_sorted = df_recommendations.sort_values('Probabilidad de Compra', ascending=True)
    ax.barh(df_sorted['Product'], df_sorted['Probabilidad de Compra'], color='skyblue')
    ax.set_xlabel('Probabilidad de Compra (%)')
    ax.set_title('Probabilidad de Compra para los Productos Recomendados')
    return fig

def recommend_main():
    """
    Lógica principal de la aplicación Streamlit.
    """
    with st.container():
        st.title('Recomendador de Productos')

        # Formulario para la selección de categoría y productos
        with st.expander(label="", expanded=True):
            col1, col2 = st.columns(2)

            with col1:
                # Selección de categorías
                categories = data_products['Category'].unique()
                selected_category = st.selectbox('Selecciona una categoría:', options=[''] + list(categories))

            with col2:
                # Activar selección de productos solo si se ha seleccionado una categoría
                if selected_category:
                    filtered_products = data_products[data_products['Category'] == selected_category]['Product'].tolist()
                    selected_products = st.multiselect('Selecciona productos:', options=filtered_products)
                else:
                    selected_products = st.multiselect('Selecciona productos:', [])

        # Botón para obtener recomendaciones
        submit_button = st.button(label='Obtener Recomendaciones')

        if submit_button and selected_category and selected_products:
            # Generar recomendaciones
            recommendations_df = genera_recomendaciones(
                selected_products,
                data_products[data_products['Category'] == selected_category]
            )
            df_recommendations = convierte_a_df_recomendaciones(recommendations_df)

            # Mostrar recomendaciones
            with st.container():
                st.title('Recomendaciones')
                with st.expander(label="", expanded=True):
                    col1, col2 = st.columns(2)

                    # Tabla con las recomendaciones
                    with col1:
                        st.dataframe(
                            df_recommendations,
                            column_config={
                                'Probabilidad de Compra': st.column_config.NumberColumn(
                                    'Probabilidad de Compra',
                                    help="Probabilidad estimada de que el usuario compre este producto.",
                                    min_value=0,
                                    max_value=100,
                                    step=1,
                                    format="%d %%",
                                )
                            },
                            hide_index=True,
                        )

                    # Gráfico de probabilidad de compra
                    with col2:
                        fig = grafica_prob_de_compra(df_recommendations)
                        st.pyplot(fig)

        elif submit_button:
            # Mensaje de error si no se seleccionaron categoría o productos
            st.write('Por favor, selecciona una categoría y al menos un producto para obtener recomendaciones.')

# Ejecutar la función principal
if __name__ == '__main__':
    recommend_main()
