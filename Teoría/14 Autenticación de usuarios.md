# 14. Autenticación de usuarios en local: Formulario propio y OAuth con Google

Al desplegar aplicaciones de IA o tableros de datos, controlar el acceso es fundamental para proteger por privacidad y por los costes de las APIs (como la de Groq que configuramos en el tema anterior).

Las cookies y el `st.session_state` son herramientas excelentes para mantener el estado, pero la autenticación requiere una lógica de control de acceso estructurada. En este tema aprenderemos dos formas de proteger nuestra aplicación en local antes de dar el salto a la nube.

---

## Estrategias de Autenticación: Formulario Propio vs. OAuth de Terceros

Para validar la identidad de un usuario en Streamlit, podemos optar por dos enfoques principales:

| Característica | Formulario de Login Propio (Usuario/Contraseña) | OAuth 2.0 (Iniciar sesión con Google) |
| --- | --- | --- |
| **Complejidad de código** | Baja (Controlado totalmente en Python con Streamlit). | Media (Requiere configurar credenciales en la consola de Google). |
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

## 2. Autenticación con OAuth de Google (Local)

Para implementar el inicio de sesión con Google de forma limpia en Streamlit sin necesidad de construir flujos complejos de redirección a mano, utilizaremos un componente de la comunidad ampliamente adoptado: `streamlit-google-auth`.

### Paso 1: Instalación del componente

Ejecuta el siguiente comando en tu terminal Linux o entorno virtual:

```bash
pip install streamlit-google-auth

```

### Paso 2: Configuración en Google Cloud Console

Para que Google permita a nuestra app local validar usuarios, debemos crear unas credenciales:

1. Ve a [Google Cloud Console](https://console.cloud.google.com/).
2. Crea un proyecto nuevo (ej. `Streamlit Local Auth`).
3. En el menú lateral, busca **API y servicios** > **Pantalla de consentimiento de OAuth**. Configúrala como *Externo* y rellena los datos básicos de soporte.
4. Ve a **Credenciales** > **Crear credenciales** > **ID de cliente de OAuth**.
5. Selecciona Tipo de aplicación: **Aplicación web**.
6. Configura las URIs de la siguiente manera para el desarrollo en local:
* **Orígenes de JavaScript autorizados:** `http://localhost:8501`
* **URIs de redireccionamiento autorizados:** `http://localhost:8501`


7. Descarga el archivo JSON generado, cámbiale el nombre a `google_credentials.json` y colócalo en la raíz del directorio de tu proyecto Streamlit.

### Paso 3: Integración del código en la aplicación de Chat

A continuación, integramos este gestor con la estructura de chat con Groq que creamos en el **Tema 13**, garantizando que el chat sólo sea accesible tras pasar el login de Google.

### Ejemplo de código: `app_protegida_google.py`

```python
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
authenticator = Authenticate(
    secret_credentials_path="google_credentials.json",
    cookie_name="google_auth_session",
    cookie_key="una_clave_secreta_y_larga_para_cookies", # Cifra la cookie en el navegador
    cookie_expiry_days=1
)

# 2. Comprobar si el usuario ya está autenticado a través de Google
authenticator.check_authentification()

# 3. Renderizar botón de login si no está autenticado
if not st.session_state.get("connected", False):
    st.title("🤖 Chatbot Corporativo")
    st.subheader("Por favor, inicia sesión para interactuar con la IA.")
    
    # Este método dibuja el botón oficial "Sign in with Google"
    authenticator.login()
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
    authenticator.logout()

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

```

---

## ⚠️ Buenas prácticas de seguridad

1. **Nunca subas credenciales a GitHub:** El archivo `google_credentials.json` y el archivo `.env` **deben** estar incluidos en tu archivo `.gitignore`.
2. **Uso de contraseñas de producción:** Si usas el método de formulario propio, no escribas la contraseña directamente en el código ("hardcoded"). Utiliza siempre `st.secrets` para leerlas desde `.streamlit/secrets.toml`.
3. **El puerto de redirección importa:** Google OAuth es estricto. Si configuras la URI en `http://localhost:8501`, tu aplicación fallará si se ejecuta por error en el puerto `8502`. Asegúrate de que el puerto de ejecución coincida exactamente con el de la consola de Google.