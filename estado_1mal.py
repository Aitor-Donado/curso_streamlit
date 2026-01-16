import streamlit as st

# Inicializar el estado de sesión si no existe
if 'form_data' not in st.session_state:
    st.session_state.form_data = {
        'name': '',
        'age': 0,
        'email': ''
    }

# Función para manejar el envío del formulario
def handle_form_submit():
    st.session_state.form_data['name'] = st.session_state.name
    st.session_state.form_data['age'] = st.session_state.age
    st.session_state.form_data['email'] = st.session_state.email
    st.success("Formulario enviado correctamente!")

# Crear el formulario
with st.form("my_form"):
    st.write("Por favor, complete el formulario:")
    
    # Campos de entrada
    st.session_state.name = st.text_input("Nombre", 
                                value=st.session_state.form_data['name'])
    st.session_state.age = st.number_input("Edad", min_value=0, 
                                max_value=120, 
                                value=st.session_state.form_data['age'])
    st.session_state.email = st.text_input("Email", 
                                value=st.session_state.form_data['email'])
    
    # Botón de envío
    submitted = st.form_submit_button("Enviar", 
                                      on_click=handle_form_submit)

# Mostrar los datos del formulario guardados en el estado de sesión
if any(st.session_state.form_data.values()):
    st.write("Datos del formulario guardados:")
    st.write(f"Nombre: {st.session_state.form_data['name']}")
    st.write(f"Edad: {st.session_state.form_data['age']}")
    st.write(f"Email: {st.session_state.form_data['email']}")
    st.divider()
    st.write("Datos de la sesión:")
    st.write(st.session_state)

# Nota: los text_input y el number_input no tienen callback.