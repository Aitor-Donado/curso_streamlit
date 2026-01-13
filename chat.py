import streamlit as st
import requests

# Función que pide a una API una cita de un famoso.
def pide_una_cita():
		response = requests.get('https://api.quotable.io/random')
		if response.status_code == 200:
			data = response.json()
			return f"{data['content']} - {data['author']}"
		else:
			return "La API no ha funcionado."

# Interfaz del chat con Streamlit
st.title("Chatbot de citas aleatorias")
user_input = st.chat_input("Envía un mensaje al chatbot")
if user_input:
		with st.chat_message('user'):
			st.write(user_input)
		with st.chat_message('assistant'):
			st.write(pide_una_cita())
				
