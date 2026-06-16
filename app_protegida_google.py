import streamlit as st
import requests
import os
from dotenv import load_dotenv

# 1. Cargar variables de entorno (Para la API de Groq)
load_dotenv()
API_KEY = os.getenv("API_KEY_GROQ")
# 2. Configurar la página (opcional, pero mejora la estética)
st.set_page_config(page_title="Chat Privado Nativo", page_icon="🤖")

# =====================================================================
# SOLUCIÓN COMPROBACIÓN: Si no hay email en st.user, no está autenticado
# =====================================================================
if not st.user.get("email"):
    st.title("🤖 Chatbot Corporativo")
    st.subheader("Por favor, inicia sesión para interactuar con la IA.")
    
    # El botón invoca el flujo de Google configurado en secrets.toml
    if st.button("Iniciar sesión con Google", type="primary"):
        st.login(provider="google")
        
    st.stop() # Detiene la app aquí si no se ha conectado el usuario

# =====================================================================
# CONTENIDO PROTEGIDO (Acceso garantizado)
# =====================================================================

# El objeto st.user contiene los claims devueltos por Google OAuth
nombre_usuario = st.user.get("name", "Usuario")
foto_usuario = st.user.get("picture", None)
email_usuario = st.user.get("email", "")

with st.sidebar:
    st.title("⚙️ Sesión Activa")
    if foto_usuario:
        st.image(foto_usuario, width=70)
    st.write(f"Conectado como: **{nombre_usuario}**")
    st.write(f"Email: `{email_usuario}`")
    st.divider()
    
    # Botón de cierre de sesión nativo
    if st.button("Cerrar Sesión"):
        st.logout()
# =====================================================================

# 3. Inicializar el historial del chat en session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Comprobar que la API key existe
if not API_KEY:
    st.error("⚠️ No se encontró la variable API_KEY_GROK en el archivo .env")
    st.stop()

# 5. Interfaz del chat
st.title(f"🤖 Chatbot con Groq. 👋 ¡Hola {nombre_usuario}! ")
# Mostrar los mensajes anteriores del historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Función para llamar a la API de Groq
def obtener_respuesta_groq(historial):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Formato que espera Groq (igual que OpenAI)
    payload = {
        "model": "llama-3.3-70b-versatile", # Puedes cambiar a "mixtral-8x7b-32768" si prefieres
        "messages": historial,
        "temperature": 0.7
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        return f"❌ Error al conectar con Groq: {response.status_code} - {response.text}"

# 7. Input del usuario y lógica del chat
user_input = st.chat_input("Escribe tu mensaje aquí...")

if user_input:
    # Añadir el mensaje del usuario al historial y mostrarlo
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generar y mostrar la respuesta del asistente
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            respuesta = obtener_respuesta_groq(st.session_state.messages)
            st.markdown(respuesta)
        
    # Añadir la respuesta al historial
    st.session_state.messages.append({"role": "assistant", "content": respuesta})