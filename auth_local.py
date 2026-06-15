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
