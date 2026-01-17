import streamlit as st
import pandas as pd
import pickle

# Cargar el modelo guardado
with open('Ejemplos/Uso_modelo_entrenado/modelo_entrenado.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Título de la aplicación
st.title("Formulario de Predicción de Salud")

# Crear un formulario para ingresar los datos
st.header("Ingrese los datos de la persona")

# Solicitar los datos
edad = st.number_input("Edad", min_value=0, max_value=120, value=47)
sexo = st.selectbox("Sexo", options=[("Hombre", 1), ("Mujer", 0)], format_func=lambda x: x[0])
presion_arterial = st.number_input("Presión arterial sistólica (ap_hi)", min_value=50, max_value=200, value=120)
colesterol_alto = st.checkbox("Colesterol alto")
glucosa_alta = st.checkbox("Glucosa alta")
bmi = st.number_input("Índice de Masa Corporal (BMI)", min_value=15.0, value=40.0)

# Convertir las opciones booleanas a 1 o 0
colesterol = 1 if colesterol_alto else 0
gluc = 1 if glucosa_alta else 0

# Crear un DataFrame con los datos ingresados
persona = pd.DataFrame(index=[0], data={
    "age": edad,
    "gender": sexo[1],
    "ap_hi": presion_arterial,
    "cholesterol": colesterol,
    "gluc": gluc,
    "BMI": bmi
})

# Mostrar los datos ingresados
st.subheader("Datos ingresados")
st.write(persona)

# Realizar la predicción
if st.button("Predecir"):
    prediccion = modelo.predict(persona)
    st.subheader("Resultado de la predicción")
    if prediccion[0] == 1:
        st.write("La persona tiene un riesgo alto.")
    else:
        st.write("La persona tiene un riesgo bajo.")
