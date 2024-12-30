# En el archivo entradas.py
import streamlit as st

#----------------------
# Primer checkbox

state = st.checkbox("Checkbox", value=True)
if state:
		st.write("Hola")
else:
		pass
#----------------------	
# Segundo checkbox

def ha_cambiado():
		"""
		Función que se ejecuta al cambiar el estado del checkbox
		"""
		print("Ha cambiado el checkbox2")
		# Imprime el estado del checkbox llamado chequeador
		print(st.session_state.chequeador)

state = st.checkbox("Checkbox2", 
					value=True, 
					on_change = ha_cambiado, 
					key = "chequeador")

st.divider()
#----------------------
# Botones radio
# Sólo permite seleccionar uno
opciones = ("España", "Cuba", "Venezuela")
radio_btn = st.radio("Marca tu país", options = opciones)
# Imprimirá el valor de la tupla seleccionado al cambiarlo
print(radio_btn)
# También se le puede asociar un "on_change" y "key" como al anterior

st.divider()
#----------------------
# Select box
# Es un selector desplegable que sólo permite una elección
opciones = ("Renault 5", "Seat 127", "Fiat 500")
select = st.selectbox("Elige tu coche favorito", options= opciones)
print(select)

st.divider()
#----------------------
# Multi Select
# Es un selector desplegable que permite varias opciones
opciones = ("Renault 5", "Seat 127", "Fiat 500")
multi_select = st.multiselect("Elige tus coches favoritos", options= opciones)
st.write(multi_select)

st.divider()
#----------------------
# Slider
valor = st.slider("Deslizante", min_value=50, max_value=150, value=75)
print(valor)

# Slider categórico
opciones = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
start_color, end_color = st.select_slider(
	'Select a range of color wavelength',
	options=opciones,
	value=('red', 'blue'))
st.write(f'Has seleccionado entre {start_color} y {end_color}')