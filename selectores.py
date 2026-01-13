# En el archivo selectores.py
import streamlit as st

st.write("# Selectores")
st.write("## Visor de estado de la sesión")
st.write(st.session_state)
st.write("Cuidado porque al arrancar desde cero, el estado de la sesión está vacío en este punto de la página")

st.divider()
st.write("## Checkbox")
#----------------------
# Primer checkbox
state = st.checkbox("Soy un Checkbox", value=True)
if state:
	st.write("¡Hola!, tienes seleccionado el checkbox")
else:
	pass

#----------------------	
# Segundo checkbox
def ha_cambiado():
	"""
	Función que se ejecuta al cambiar el estado del segundo checkbox
	"""
	print("Ha cambiado el checkbox2")
	# Imprime el estado del checkbox llamado chequeador
	print("El valor del checkbox es: ", st.session_state.chequeador)


state = st.checkbox("Checkbox2", 
					value=True, 
					on_change = ha_cambiado, 
					key = "chequeador")


st.divider()


#----------------------
st.write("## Radio Button")
# Sólo permite seleccionar uno
opciones = ("España", "Cuba", "Venezuela")
radio_btn = st.radio("Marca tu país", options = opciones)
# Imprimirá el valor de la tupla seleccionado al cambiarlo
st.write(radio_btn)
print(radio_btn)
# También se le puede asociar un "on_change" y "key" como al anterior

st.divider()
#----------------------
st.write("## Select box")
# Es un selector desplegable que sólo permite una elección
opciones = ("Renault 5", "Seat 127", "Fiat 500")
select = st.selectbox("Elige tu coche favorito", options= opciones, key="coche")
print(select)

st.divider()
#----------------------
st.write("## Multi Select")
# Es un selector desplegable que permite varias opciones
opciones = ("Renault 5", "Seat 127", "Fiat 500")
multi_select = st.multiselect("Elige tus coches favoritos", options= opciones, key="coches")
st.write(multi_select)

st.divider()
#----------------------
st.write("## Slider")
valor = st.slider("Control deslizante", min_value=50, max_value=150, value=75)
print(valor)

st.divider()

# Slider categórico
st.write("## Slider categórico")
opciones = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
start_color, end_color = st.select_slider(
	'Selecciona un color de la gama de longitudes de onda',
	options=opciones,
	value=('red', 'blue'))

st.write(f'Has seleccionado entre {start_color} y {end_color}')

st.divider()

st.write("## Visor de estado de la sesión")
st.write(st.session_state)
st.write("En cambio, al final de la página, la sesión ya tiene todos los keys de los objetos que han ido creándose")
