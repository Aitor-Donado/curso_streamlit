import streamlit as st
import os
from dotenv import load_dotenv

# Cargar variables de entorno (Para la API de Groq)
load_dotenv()
API_KEY = os.getenv("API_KEY_GROQ")

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

# Interfaz del chat normal con Groq...
st.title(f"👋 ¡Hola {nombre_usuario}! Chat con Groq habilitado")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Escribe tu consulta al LLM...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
        
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            respuesta = f"Hola {nombre_usuario}, tu sesión está protegida mediante el sistema nativo de Streamlit."
            st.markdown(respuesta)
            
    st.session_state.messages.append({"role": "assistant", "content": respuesta})