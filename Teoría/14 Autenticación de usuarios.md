# 14. Autenticación de usuarios en local: Formulario propio y OAuth Nativo con Google

Al desplegar aplicaciones de IA o tableros de datos, controlar el acceso es fundamental para proteger la privacidad y mitigar los costes de las APIs (como la de Groq que configuramos en el tema anterior).

Las cookies y el `st.session_state` son herramientas excelentes para mantener el estado, pero la autenticación requiere una lógica de control de acceso estructurada. En este tema aprenderemos dos formas de proteger nuestra aplicación en local antes de dar el salto a la nube.

---

## Estrategias de Autenticación: Formulario Propio vs. OAuth de Terceros

Para validar la identidad de un usuario en Streamlit, podemos optar por dos enfoques principales:

| Característica | Formulario de Login Propio (Usuario/Contraseña) | OAuth 2.0 Nativo (Iniciar sesión con Google) |
| --- | --- | --- |
| **Complejidad de código** | Baja (Controlado totalmente en Python con Streamlit). | Baja-Media (Configuración en la consola de Google y `.streamlit/secrets.toml`). |
| **Experiencia de usuario** | El usuario debe registrarse y recordar otra contraseña. | Un solo clic usando una cuenta que el usuario ya posee. |
| **Seguridad de credenciales** | Responsabilidad del desarrollador (cifrado, almacenamiento). | Delegada en Google (máxima seguridad, soporte MFA). |
| **Uso ideal** | Prototipos rápidos, aplicaciones internas muy reducidas. | Aplicaciones de producción, entornos corporativos o públicos. |

---

## 1. Autenticación Local con Formulario Propio

Para implementar un sistema básico en local, combinaremos el uso de **`st.form`** para evitar recargas innecesarias al escribir, **`st.session_state`** para recordar que el usuario se ha autenticado con éxito, y funciones de utilidad de control de flujo como **`st.stop()`**.

### Ejemplo de código: `auth_local.py`

```python
import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="App Protegida", page_icon="🔐")

# 2. Inicializar el estado de autenticación si no existe
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

# 3. Función para verificar las credenciales
def verificar_credenciales(usuario, password):
    # NOTA: En producción, nunca guardes contraseñas en texto plano. 
    # Usa st.secrets o librerías de hashing como bcrypt.
    USUARIO_CORRECTO = "profesor"
    PASSWORD_CORRECTO = "streamlit2026"
    
    if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTO:
        st.session_state.autenticado = True
        st.success("¡Acceso concedido!")
        st.rerun() # Forzar recarga para mostrar el contenido protegido
    else:
        st.error("❌ Usuario o contraseña incorrectos.")

# 4. Renderizar el formulario si no está autenticado
if not st.session_state.autenticado:
    st.title("🔐 Iniciar Sesión")
    
    # Usamos st.form para agrupar los inputs de forma colectiva
    with st.form(key="formulario_login"):
        usuario_input = st.text_input("Usuario")
        password_input = st.text_input("Contraseña", type="password")
        boton_enviar = st.form_submit_button("Entrar")
        
    if boton_enviar:
        verificar_credenciales(usuario_input, password_input)
        
    # Detenemos la ejecución del script aquí para que nadie vea el contenido
    st.stop()

# =====================================================================
# CONTENIDO PROTEGIDO (Solo se ejecuta si st.session_state.autenticado == True)
# =====================================================================
st.title("🤖 Panel de Control de nuestra IA")
st.write(f"Bienvenido al sistema. Tu token de Groq está seguro aquí.")

# Botón para cerrar sesión
if st.button("Cerrar Sesión"):
    st.session_state.autenticado = False
    st.rerun()

```

---

## 2. Autenticación con OAuth de Google (Sistema Nativo)

Streamlit incorpora soporte nativo para autenticación OAuth sin necesidad de recurrir a componentes externos obsoletos. Utilizando las funciones `st.login()`, `st.logout()` y el objeto de contexto `st.user`, podemos securizar aplicaciones delegando la gestión de identidad en Google.

### Paso 1: Instalación de dependencias

El sistema nativo requiere instalar el paquete de autenticación de Streamlit junto con un cliente HTTP compatible (`httpx`). Ejecuta el siguiente comando en tu terminal Linux o entorno virtual:

```bash
pip install httpx streamlit[auth]

```

### Paso 2: Configuración en Google Cloud Console

Para que Google permita a nuestra aplicación local validar a los usuarios, debemos configurar las credenciales del proyecto:

1. Ve a [Google Cloud Console](https://console.cloud.google.com/).
2. Crea un proyecto nuevo (ej. `Streamlit Local Nativo`).
3. En el menú lateral, busca **API y servicios** > **Pantalla de consentimiento de OAuth**. Configúrala como *Externo* y rellena los datos básicos de soporte de la aplicación.
4. Ve a **Credenciales** > **Crear credenciales** > **ID de cliente de OAuth**.
5. Selecciona Tipo de aplicación: **Aplicación web**.
6. Configura las URIs de forma estricta para el entorno de desarrollo local:
* **Orígenes de JavaScript autorizados:** `http://localhost:8501`
* **URIs de redireccionamiento autorizados:** `http://localhost:8501/oauth2callback`



> ⚠️ **Nota crítica:** El sistema nativo de Streamlit procesa el retorno de credenciales obligatoriamente a través de la ruta `/oauth2callback`.

### Paso 3: Configuración de Secretos locales (`secrets.toml`)

Crea o edita tu archivo de secretos dentro del directorio de tu proyecto en la ruta `.streamlit/secrets.toml`. Es indispensable estructurar los parámetros exactamente bajo los bloques indicados para que Streamlit los mapee de forma automática:

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "una_cadena_muy_larga_y_completamente_aleatoria_para_cifrar_las_cookies_129387"

# Es fundamental que estas claves de Google estén exactamente bajo [auth.google]
[auth.google]
client_id = "1234567890-xxxxxxxx.apps.googleusercontent.com"
client_secret = "xxxxxxxxxxxx"
server_metadata_url = "[https://accounts.google.com/.well-known/openid-configuration](https://accounts.google.com/.well-known/openid-configuration)"

```

### Paso 4: Integración del código en la aplicación de Chat

Integramos el flujo nativo con la estructura de chat con Groq que creamos en el **Tema 13**. Validaremos el estado del usuario consultando las propiedades del objeto especial `st.user`.

### Ejemplo de código: `app_protegida_google.py`

```python
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

# Barra lateral con información del usuario y botón de Logout
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
            respuesta = f"Hola {nombre_usuario}, tu sesión está protegida mediante el sistema nativo de Streamlit."
            st.markdown(respuesta)
            
    st.session_state.messages.append({"role": "assistant", "content": respuesta})

```

---

## ⚠️ Buenas prácticas de seguridad

1. **Nunca subas credenciales a GitHub:** Los archivos `.streamlit/secrets.toml` y `.env` **deben** incluirse de forma estricta en tu archivo `.gitignore`.
2. **Uso de contraseñas de producción:** Si empleas el método de formulario propio, no expongas las credenciales directamente en el código ("hardcoded"). Centraliza las variables utilizando `st.secrets`.
3. **El puerto y la ruta de redirección importan:** Google OAuth rechaza peticiones si los parámetros difieren un solo carácter. Si configuras la URI en `http://localhost:8501/oauth2callback`, tu aplicación fallará si se ejecuta en otro puerto (ej. `8502`) o si omites la terminación `/oauth2callback` exigida por el framework.
