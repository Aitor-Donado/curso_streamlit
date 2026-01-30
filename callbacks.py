import streamlit as st

# Definición de la función callback
if 'show_message' not in st.session_state:
	st.session_state.show_message = False

def toggle_message():
	st.session_state.show_message = not st.session_state.show_message

# Crear un botón y asociarle la ejecución del callback
st.button("Toggle Message", on_click=toggle_message)

# Elemento condicional basado en el efecto del callback en el estado de sesión
if st.session_state.get('show_message', False):
	st.write("Hello, Streamlit!")
	
# Mostrar el estado de sesión
st.write(st.session_state)

# import streamlit as st

# === INICIALIZACIÓN DEL ESTADO ===
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_age" not in st.session_state:
    st.session_state.user_age = 0
if "submission_result" not in st.session_state:
    st.session_state.submission_result = None

# === CALLBACK: procesa y guarda resultado ===
def process_form():
    # Los valores ya existen en session_state gracias a los keys de los inputs
    name = st.session_state.user_name
    age = st.session_state.user_age
    
    # Procesamiento (puede ser validación, cálculo, etc.)
    if name and age > 0:
        st.session_state.submission_result = {
            "name": name,
            "age": age,
            "status": "✅ Formulario procesado correctamente"
        }
    else:
        st.session_state.submission_result = {
            "status": "❌ Por favor completa todos los campos"
        }

# === FORMULARIO ===
st.title("Formulario con Callback")

with st.form("user_form", clear_on_submit=True):
    st.text_input("Enter your name", key="user_name")
    st.number_input("Enter your age", min_value=0, max_value=100, step=1, key="user_age")
    st.form_submit_button("Submit", on_click=process_form)

# === VISUALIZACIÓN DEL RESULTADO ===
if st.session_state.submission_result:
    st.divider()
    st.subheader("Resultado del procesamiento:")
    result = st.session_state.submission_result
    
    if "name" in result:
        st.write(f"**Name:** {result['name']}")
        st.write(f"**Age:** {result['age']}")
    
    st.info(result["status"])