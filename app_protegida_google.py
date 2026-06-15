import streamlit as st
import os
from dotenv import load_dotenv
from streamlit_google_auth import Authenticate

# Cargar variables de entorno (Para la API de Groq)
load_dotenv()
API_KEY = os.getenv("API_KEY_GROQ")

st.set_page_config(page_title="Chat Privado con Google", page_icon="🤖")

# 1. Inicializar el autenticador usando el JSON de Google Cloud
# El componente se encarga de gestionar internamente las cookies y el session_state

if "authenticator" not in st.session_state:
    st.session_state.authenticator = Authenticate(
        secret_credentials_path="google_credentials.json",
        cookie_name="google_auth_session",
        cookie_key="una_clave_secreta_y_larga_para_cookies", # Cifra la cookie en el navegador
        cookie_expiry_days=1,
        redirect_uri="http://localhost:8501"  # <--- Añade esta línea exacta
    )

# 2. Comprobar si el usuario ya está autenticado a través de Google
st.session_state.authenticator.check_authentification()

# 3. Renderizar botón de login si no está autenticado
if not st.session_state.get("connected", False):
    st.title("🤖 Chatbot Corporativo")
    st.subheader("Por favor, inicia sesión para interactuar con la IA.")
    
    # Este método dibuja el botón oficial "Sign in with Google"
    st.session_state.authenticator.login()
    st.stop() # Detiene la app aquí si no se ha conectado

# =====================================================================
# CONTENIDO PROTEGIDO (Solo accesible si el login con Google fue exitoso)
# =====================================================================

# Podemos recuperar información del perfil de Google del usuario desde el session_state
user_info = st.session_state.get("user_info", {})
nombre_usuario = user_info.get("name", "Usuario de Google")
foto_usuario = user_info.get("picture", None)

# Barra lateral con información del usuario y botón de Logout
with st.sidebar:
    st.title("⚙️ Sesión Activa")
    if foto_usuario:
        st.image(foto_usuario, width=70)
    st.write(f"Conectado como: **{nombre_usuario}**")
    st.write(f"Email: `{user_info.get('email')}`")
    st.divider()
    
    # Botón para revocar el token y salir
    st.session_state.authenticator.logout()

# Interfaz del chat (Código heredado del Punto 13)
st.title(f"👋 ¡Hola {nombre_usuario}! Chat con Groq habilitado")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada de texto del chat
user_input = st.chat_input("Escribe tu consulta al LLM...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
        
    # Aquí vendría la llamada a obtener_respuesta_groq() vista en el tema anterior...
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            # Simulación de respuesta para el entorno local
            respuesta = f"Hola {nombre_usuario}, recibí tu mensaje: '{user_input}'. Tu sesión está securizada con OAuth."
            st.markdown(respuesta)
            
    st.session_state.messages.append({"role": "assistant", "content": respuesta})