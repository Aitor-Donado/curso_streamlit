# 05. Widgets de entrada. Texto

Introducción de datos mediante `st.text_input()`, `st.text_area()`, `st.number_input()`, `st.date_input()`, `st.time_input()`

## Text input

```python
# streamlit run  intro_texto_estado.py
import streamlit as st
import datetime

# Creamos una función que imprima en consola los datos introducidos
def imprime_estado():
    "Al ejecutarse esta función el estado de la sesión no se habrá actualizado"
    print("Estado de la sesión:")
    print(st.session_state)

st.session_state.texto_corto = st.text_input("Introduce un texto", 
                                             max_chars=60, 
                                             on_change = imprime_estado)

st.json(st.session_state)
```

Para que la función `imprime_estado()` use el estado actualizado, hay que añadir el parámetro `key` al elemento, no guardar directamente el `text_input` a `st.session_state.texto_corto`.

```python
# En el archivo intro_texto_estado2.py
import streamlit as st
import datetime

# Inicializar si no existe
if 'mi_texto' not in st.session_state:
    st.session_state.mi_texto = ""

def manejar_cambio():
    print(f"Texto cambiado a: {st.session_state.mi_texto}")
    # Aquí puedes realizar otras operaciones con el nuevo valor

st.text_input("Introduce texto", 
             value=st.session_state.mi_texto,
             key="mi_texto",
             on_change=manejar_cambio)

st.write("Valor actual:", st.session_state.mi_texto)
```

### Text area

```python
st.session_state.texto_largo = st.text_area("Introduce un texto largo", 
                                      on_change = imprime_estado)
```

### Number Input

```python
st.session_state.numero_entero = st.number_input('Introduce un número', 
                                                min_value=10, 
                                                max_value=100, 
                                                on_change = imprime_estado)
```

### Date Input

```python
st.session_state.fecha = st.date_input("Introduce una fecha", 
                                      on_change = imprime_estado)
```

### Time Input

```python
st.session_state.hora = st.time_input("Introduce una hora", step = datetime.timedelta(minutes=5), 
                                on_change = imprime_estado)
```

### Date Input con restricción de fechas

```python
# Permitir elegir un rango de fechas
today = datetime.date.today()
last_week = today - datetime.timedelta(days=7)

st.session_state.rango_fechas = st.date_input("Selecciona el rango de fechas ",
    value = (last_week ,today),
    min_value = datetime.date(2012, 12, 1),
    max_value = datetime.date.today(), format="MM.DD.YYYY", 
                                      on_change = imprime_estado)
```

También podemos imprimir en pantalla los datos guardados.

```python
st.json(st.session_state)
```
