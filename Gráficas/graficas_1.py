import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.divider()
# Bar chart
st.write('Gráfico de barras `st.bar_chart(df, x="Categorías", y="Valores")`')
bar_data = {'Categorías': ['A', 'B', 'C'], 
            'Valores': [10, 20, 30]}
df = pd.DataFrame(bar_data)
st.bar_chart(df, x="Categorías", y="Valores")

st.divider()
# Line chart
st.write('Gráfico de línes `st.line_chart(line_data.set_index("Date"))`')
line_data = pd.DataFrame({'Date': pd.date_range(start='1/1/2020', periods=30), 
                          'Value': np.random.randn(30).cumsum()})
st.line_chart(line_data.set_index('Date'))

st.divider()
# Area chart
st.write('Gráfico de área `st.area_chart(area_data.set_index("Time"))`')
area_data = pd.DataFrame({'Time': range(1, 11), 
                          'Value': np.random.randn(10).cumsum()})
st.area_chart(area_data.set_index('Time'))

st.divider()
# Scatter chart
st.write('Gráfico de dispersión `st.scatter_chart(data)`')
data = pd.DataFrame(np.random.randn(100, 2), columns= ['A', 'B'])
st.scatter_chart(data)

st.divider()
# Mapa
st.write('Mapa `st.map(data)`')
data = pd.DataFrame({'lat': [43.26093, 43.296782], 'lon': [-2.93611, -1.895542]})
st.map(data)

st.divider()
# Gráfico de línea con Plotly
st.write('Gráfico de línea con Plotly')
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Sine wave'))
fig.update_layout(title='Gráfico del seno(x) con Plotly',
                xaxis_title='x',
                yaxis_title='sin(x)')

st.plotly_chart(fig)

st.divider()
# Grafo de graphviz
st.write('Grafo de graphviz `st.graphviz_chart(graph)`')
graph = """
digraph { a -> b; b -> c; c -> d;
        c -> e; d -> a;e -> f;f -> b;}"""
st.graphviz_chart(graph)