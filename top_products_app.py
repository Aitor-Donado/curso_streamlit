import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Función para cargar los datos del archivo CSV
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Cargar los datos de ventas
sales_df = load_data('data/product_sales.csv')
# Convertir la columna 'Order Date' a formato datetime
sales_df['Order Date'] = pd.to_datetime(sales_df['Order Date'])

def serie_temp_ventas(sales_df):
    """
    Genera un gráfico que muestra las ventas totales a lo largo del tiempo.
    """
    sales_over_time = sales_df.groupby(sales_df['Order Date'].dt.to_period('M')).agg({'Price': 'sum'})
    sales_over_time.reset_index(inplace=True)
    sales_over_time['Order Date'] = sales_over_time['Order Date'].dt.to_timestamp()

    plt.figure(figsize=(10, 5))
    plt.plot(sales_over_time['Order Date'], sales_over_time['Price'], marker='o', linestyle='-')
    plt.title('Ventas a lo largo del tiempo')
    plt.xlabel('Fecha de pedido')
    plt.ylabel('Ventas totales ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    st.pyplot(plt)

def plot_customer_demographics(sales_df):
    """
    Genera gráficos para la distribución de edad y género de los clientes.
    """
    fig_size = (6, 4)

    # Gráfico de histograma para la distribución de edades
    fig_age, ax_age = plt.subplots(figsize=fig_size)
    ax_age.hist(sales_df['User Age'], bins=10, edgecolor='black')
    ax_age.set_title('Distribución de edades de los clientes')
    ax_age.set_xlabel('Edad')
    ax_age.set_ylabel('Frecuencia')

    # Gráfico de pastel para la distribución de género
    fig_gender, ax_gender = plt.subplots(figsize=fig_size)
    gender_counts = sales_df['User Gender'].value_counts()
    ax_gender.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
    ax_gender.set_title('Distribución de género de los clientes')

    plt.tight_layout()
    return fig_age, fig_gender

def plot_top_products(sales_df):
    """
    Genera un gráfico que muestra los productos más vendidos por cantidad.
    """
    top_products = sales_df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(10)

    fig_top, ax_top = plt.subplots()
    sns.barplot(x=top_products.values, y=top_products.index, ax=ax_top)
    ax_top.set_title('Productos más vendidos por cantidad')
    ax_top.set_xlabel('Cantidad vendida')
    ax_top.set_ylabel('Producto')
    st.pyplot(fig_top)

def calculate_clv(sales_df):
    """
    Calcula y muestra el valor del cliente a lo largo del tiempo (CLV).
    """
    revenue_per_user = sales_df.groupby('User ID')['Price'].sum().mean()
    st.metric(label="Valor del cliente a lo largo del tiempo (CLV)", value=f"${revenue_per_user:.2f}")

def calculate_aov(sales_df):
    """
    Calcula y muestra el valor promedio por pedido (AOV).
    """
    total_revenue = sales_df['Price'].sum()
    total_orders = sales_df.shape[0]
    aov = total_revenue / total_orders
    st.metric("Valor promedio por pedido (AOV)", f"${aov:.2f}")

def calculate_purchase_frequency(sales_df):
    """
    Calcula y muestra la frecuencia de compra.
    """
    total_orders = sales_df.shape[0]
    unique_customers = sales_df['User ID'].nunique()
    purchase_frequency = total_orders / unique_customers
    definicion = """Frecuencia de compra
    (pedidos por cliente)"""
    st.metric(definicion, f"{purchase_frequency:.2f}")

def top_products_main():
    """
    Función principal para generar los insights y visualizaciones.
    """
    st.title('Análisis de Ventas y Productos')

    # Métricas principales
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander(label="", expanded=True):
            calculate_clv(sales_df)

    with col2:
        with st.expander(label="", expanded=True):
            calculate_aov(sales_df)

    with col3:
        with st.expander(label="", expanded=True):
            calculate_purchase_frequency(sales_df)

    # Ventas a lo largo del tiempo
    st.header('Insights de Ventas')
    with st.expander(label="", expanded=True):
        serie_temp_ventas(sales_df)

    # Distribución de clientes
    st.header('Distribución de Clientes')
    col21, col22 = st.columns(2)

    fig_age, fig_gender = plot_customer_demographics(sales_df)

    with col21:
        with st.expander(label="", expanded=True):
            st.pyplot(fig_gender)

    with col22:
        with st.expander(label="", expanded=True):
            st.pyplot(fig_age)

    # Productos más vendidos
    st.header('Productos Más Vendidos')
    with st.expander(label="", expanded=True):
        plot_top_products(sales_df)

# Ejecutar la aplicación principal
if __name__ == '__main__':
    top_products_main()
