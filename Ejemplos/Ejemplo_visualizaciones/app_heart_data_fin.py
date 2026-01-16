import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from app_con_datos import aplicacion_con_uploaded_file

st.title("Inspección de datos de .csv")

uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

if uploaded_file is None:
    st.info("Por favor, sube un archivo CSV para comenzar.")
else:
    with st.container():
        aplicacion_con_uploaded_file(uploaded_file)
    