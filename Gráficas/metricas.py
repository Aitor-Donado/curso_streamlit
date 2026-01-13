import streamlit as st
col1, col2, col3 , col4= st.columns(4)

col1.metric("Temperature", "26 °C", "1.2 °F")
col2.metric("Wind", "20 mph", "-8%")
col3.metric("Humidity", "16%", "4%")
col4.metric("Rain", "6%", "10%")