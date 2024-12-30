import streamlit as st
import datetime

valor = st.text_input("Introduce un texto", max_chars=60)
print(valor)

valor = st.text_area("Introduce un texto largo")
print(valor)

valor = st.number_input('Introduce un número', min_value=10, max_value=100)
print(valor)

valor = st.date_input("Introduce una fecha")
print(valor)

# Permitir elegir dentro de un rango dado
today = datetime.date.today()
last_week = today - datetime.timedelta(days=7)
st.date_input("Selecciona el rango de fechas ",
		value = (last_week ,today),
		min_value = datetime.date(2022, 12, 1),
		max_value = datetime.date.today(), format="MM.DD.YYYY",
)

valor = st.time_input("Introduce una hora")
print(valor)
