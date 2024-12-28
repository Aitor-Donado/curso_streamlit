import streamlit as st
import random
import pandas as pd
# Sample product data
products = ['Phone', 'Laptop', 'Headphones', 'Camera',
    'Smartwatch', 'Tablet', 'Charger', 'Keyboard', 'Mouse',
    'Speaker']
# Product data with categories
product_categories = {
    'Educational': ['Book', 'Online Course',
    'Educational Toy', 'Science Kit', 'Math Workbook',
    'Language Learning Software'],
    'Travel': ['Luggage', 'Travel Pillow', 'World Map',
        'Travel Guidebook', 'Portable Charger', 'Travel Backpack'],
    'Books': ['Fiction', 'Non-Fiction', 'Biography', 'Mystery', 
        'Science Fiction', 'Historical Fiction', 'Self-Help'],
    'Gadgets': ['Phone', 'Headset', 'Smartwatch', 'Laptop', 
        'Tablet', 'E-reader', 'Portable Speaker', 'Fitness Tracker'],
    'Home & Kitchen': ['Coffee Maker', 'Blender',
    'Smart Home Device', 'Cookware Set', 'Decorative Vase',
    'Bedding Set'],
    'Fashion': ['T-shirt', 'Jeans', 'Dress', 'Watch',
        'Handbag', 'Sneakers', 'Sunglasses', 'Jacket'],
    'Health & Wellness': ['Yoga Mat', 'Fitness Band',
        'Protein Powder', 'Skincare Product', 'Haircare Kit',
        'Vitamins', 'Aromatherapy Diffuser']
    }

def generate_random_recommendations(selected_products, products, num_recommendations = 3):
    """Generate random product recommendations."""
    available_products = [p for p in products if p not in selected_products]
    recommendations = random.sample(available_products, min(num_recommendations, len(available_products)))
    return recommendations

def create_recommendation_df(recommendations):
    """Create a DataFrame with recommendations and
    random likelihood percentages."""
    # Random likelihood percentages between 50% and 99%
    likelihoods = [random.randint(50, 99) for _ in recommendations]
    return pd.DataFrame({'Recommended Product': recommendations, 'Probabilidad de compra': likelihoods})


configuracion_columna = {'Probabilidad de compra':st.column_config.NumberColumn(
                                'Probabilidad de compra', 
                                help="Probabilidad de que te guste este **producto**",
                                min_value=0,
                                max_value=100,
                                step=1,
                                format="%d %%")}

def recommend_main():
    with st.container():
        st.title('Product Recommender')
        # Form for category and product selection
        with st.expander(label="", expanded = True):
            col1, col2 = st.columns(2)
            with col1:
                opciones = [''] + list(product_categories.keys())
                selected_category = st.selectbox('Choose category:', options=opciones)
            with col2:
                # Al elegir una categoría se puede elegir los productos
                if selected_category:
                    productos = product_categories[selected_category]
                else:
                    productos = []
                selected_products = st.multiselect('Elija productos:', productos)
            # Submit button for the form
            submit_button = st.button(label='Obtener Recomendaciones')
        if submit_button and selected_category and selected_products:
            recommendations = generate_random_recommendations(selected_products, product_categories[selected_category])
            df_recommendations = create_recommendation_df(recommendations)
            st.write('Productos recomendados:')
            st.dataframe(df_recommendations,
                        column_config=configuracion_columna,
                        hide_index=True)
        elif submit_button:
            st.write('Elija una categoría y un producto para ver las recomendaciones.')