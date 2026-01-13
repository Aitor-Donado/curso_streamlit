import streamlit as st
import datetime

# Creamos una función que imprima en consola los datos introducidos
def imprime_estado():
    "Al ejecutarse esta función el estado de la sesión no se habrá actualizado"
    print("Estado de la sesión:")
    print(st.session_state)

st.session_state.texto_corto = st.text_input("Introduce un texto", 
                                             max_chars=60, 
                                             on_change = imprime_estado)

st.write(st.session_state.texto_corto)

st.session_state.texto_largo = st.text_area("Introduce un texto largo", 
                                      on_change = imprime_estado)

st.session_state.numero_entero = st.number_input('Introduce un número', 
                                                min_value=10, 
                                                max_value=100, 
                                                on_change = imprime_estado)

st.session_state.fecha = st.date_input("Introduce una fecha", 
                                      on_change = imprime_estado)

st.session_state.hora = st.time_input("Introduce una hora", 
                                      step = datetime.timedelta(minutes=5), 
                                      on_change = imprime_estado)

# Permitir elegir un rango de fechas
today = datetime.date.today()
last_week = today - datetime.timedelta(days=7)

st.session_state.rango_fechas = st.date_input("Selecciona el rango de fechas ",
    value = (last_week ,today),
    min_value = datetime.date(2022, 12, 1),
    max_value = datetime.date.today(), format="MM.DD.YYYY", 
                                      on_change = imprime_estado)

# Imprimimos en pantalla el estado de sesión
st.json(st.session_state)