# 04. Widgets de entrada. Selectores.

Veremos el uso de widgets básicos:  `st.checkbox()`, `st.radio()`, `st.selectbox()`, `st.multiselect()`, `st.slider()`,

Nos detendremos especialmente en el primero, `st.checkbox()` para introducir el concepto de estado. Los demás, simplemente los enunciaremos.

### 3.1. Checkbox

- Código
    
    ```python
    # En el archivo selectores.py
    import streamlit as st
    
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
    	print(st.session_state.chequeador)
    
    state = st.checkbox("Checkbox2", 
    					value=True, 
    					on_change = ha_cambiado, 
    					key = "chequeador")
    ```
    

Este código de Streamlit demuestra el uso de checkboxes y cómo reaccionar a sus cambios de estado.

**Primera parte:**

Esta primera parte crea un checkbox y muestra el mensaje "Hola" en la aplicación solo si el checkbox está marcado.

```python
# En el archivo selectores.py
import streamlit as st

state = st.checkbox("Soy un Checkbox", value=True)
if state:
	st.write("¡Hola!, tienes seleccionado el checkbox")
else:
	pass
```

- `import streamlit as st`: Importa la librería Streamlit y la asigna el alias `st` para facilitar su uso.
- `state = st.checkbox("Checkbox", value=True)`: Crea un checkbox en la aplicación.
    - `"Checkbox"`: Es la etiqueta de texto que se muestra junto al checkbox.
    - `value=True`: Establece el estado inicial del checkbox como marcado (checked).
    - El valor del checkbox (True o False) se almacena en la variable `state`.
- `if state:`: Verifica el valor de la variable `state`.
    - Si `state` es `True` (el checkbox está marcado), se ejecuta `st.write("Hola")`, que muestra el texto "Hola" en la aplicación.
    - `else: pass`: Si `state` es `False` (el checkbox no está marcado), no se hace nada. `pass` es una instrucción nula en Python.

**Segunda parte:**

La segunda parte crea un checkbox que, además de mostrarse en la interfaz, ejecuta la función `ha_cambiado()` cada vez que se modifica su estado. Esta función imprime un mensaje en la consola y el valor actual del checkbox (True o False).

```python
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
```

- `def ha_cambiado():`: Define una función llamada `ha_cambiado()`. Esta función se ejecutará cada vez que cambie el estado del checkbox.
    - `print("Ha cambiado el checkbox")`: Imprime un mensaje en la consola indicando que se ha detectado un cambio en el checkbox.
    - `print(st.session_state.chequeador)`: Accede al estado actual del checkbox a través de `st.session_state`.
        - `st.session_state`: Es un diccionario que almacena el estado de los widgets de Streamlit a lo largo de las interacciones del usuario.
        - `chequeador`: Es la clave (key) que se utiliza para identificar el estado de este checkbox en particular dentro de `st.session_state`.
- `state = st.checkbox(...)`: Vuelve a crear un checkbox, pero esta vez con parámetros adicionales:
    - `on_change = ha_cambiado`: Asigna la función `ha_cambiado` al evento de cambio del checkbox. Esto significa que `ha_cambiado()` se ejecutará automáticamente cada vez que el usuario marque o desmarque el checkbox.
    - `key = "chequeador"`: Asigna la clave `"chequeador"` a este checkbox dentro de `st.session_state`. Esto es crucial para poder acceder a su valor actual dentro de la función `ha_cambiado()`.

**Diferencias clave entre las dos partes:**

- La primera parte solo muestra un mensaje en la interfaz gráfica (`st.write()`) si el checkbox está marcado en el momento de la ejecución inicial del script. No reacciona a cambios posteriores.
- La segunda parte utiliza la funcionalidad `on_change` y `st.session_state` para ejecutar una función (`ha_cambiado()`) cada vez que el usuario interactúa con el checkbox, mostrando información en la consola.

La segunda forma es la recomendada para interacciones más complejas, permitiendo mantener el estado y realizar acciones basadas en cambios en los widgets.

### 3.2. radio_btn

```python
# En el archivo selectores.py
import streamlit as st

# Sólo permite seleccionar uno
opciones = ("España", "Cuba", "Venezuela")
radio_btn = st.radio("Marca tu país", options = opciones)
# Imprimirá el valor de la tupla seleccionado al cambiarlo
print(radio_btn)
# También se le puede asociar un "on_change" y "key" como al anterior
```

### 3.3. selectbox

```python
# En el archivo selectores.py
import streamlit as st

# Es un selector desplegable que sólo permite una elección
opciones = ("Renault 5", "Seat 127", "Fiat 500")
select = st.selectbox("Elige tu coche favorito", options= opciones)
print(select)
```

### 3.4. multiselect

```python
# En el archivo selectores.py
import streamlit as st

# Es un selector desplegable que permite varias opciones
opciones = ("Renault 5", "Seat 127", "Fiat 500")
multi_select = st.multiselect("Elige tus coches favoritos", options=opciones)
st.write(multi_select)
```

### 3.5. slider

```python
# En el archivo selectores.py
valor = st.slider("Deslizante", min_value=50, max_value=150, value=75)
print(valor)
```

### 3.6. select_slider

```python
# En el archivo selectores.py
opciones = ['infrared', 'red', 'orange', 'yellow', 'green', 
            'blue', 'indigo', 'violet', 'ultraviolet']
start_color, end_color = st.select_slider('Selecciona una gama de colores',
                                            options=opciones,
                                            value=('red', 'blue'))
st.write(f'Has seleccionado entre {start_color} y {end_color}')
```