import streamlit as st
import random
import time

# Configuración de la página
st.set_page_config(page_title="Demo: stop() vs rerun()", page_icon="⏸️🔄", layout="wide")

# Inicialización del estado de sesión
if 'contador_rerun' not in st.session_state:
    st.session_state.contador_rerun = 0
if 'numero_aleatorio' not in st.session_state:
    st.session_state.numero_aleatorio = random.randint(1, 100)
if 'historial_numeros' not in st.session_state:
    st.session_state.historial_numeros = [st.session_state.numero_aleatorio]
if 'texto_guardado' not in st.session_state:
    st.session_state.texto_guardado = ""

# Título y descripción
st.title("⏸️🔄 Demostración: stop() vs rerun() en Streamlit")
st.markdown("""
Esta aplicación muestra la diferencia fundamental entre dos funciones de control de flujo en Streamlit:
`st.stop()` y `st.rerun()`. Ambas afectan la ejecución de la aplicación, pero de maneras muy diferentes.
""")

# Crear columnas para organizar el contenido
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.header("⏸️ Función: `st.stop()`")
    st.markdown("""
    **`st.stop()`** detiene inmediatamente la ejecución de la aplicación en ese punto.
    
    - Todo el código que venga después de `st.stop()` **NO se ejecutará**
    - La aplicación se "congela" en el estado actual
    - No se pueden actualizar widgets después del punto de detención
    - Para continuar, el usuario debe desactivar la condición que causó el `stop()`
    """)
    
    st.divider()
    
    # Demostración de st.stop()
    st.subheader("Demo: Efecto de `stop()`")
    
    st.markdown("Marca la casilla a continuación para activar `st.stop()`:")
    
    # Checkbox para activar stop()
    if st.checkbox("Activar stop()", key="stop_checkbox"):
        st.warning("¡stop() activado! La ejecución se detendrá aquí.")
        st.info("""
        **Observa que:**
        1. El número aleatorio NO se regenera
        2. El formulario de abajo NO se puede usar
        3. El contador NO se actualiza
        """)
        st.stop()  # ¡La ejecución se detiene aquí!
    
    # Código después de stop() - solo se ejecuta si stop() no se activó
    st.success("✅ `stop()` NO está activado. Todo el código después se ejecuta normalmente.")
    
    # Mostrar número aleatorio actual
    st.metric(label="Número aleatorio actual", value=st.session_state.numero_aleatorio)
    
    # Explicación de lo que sucede con stop()
    with st.expander("📖 ¿Qué está pasando aquí?"):
        st.markdown("""
        **Sin `stop()` activado:**
        - Streamlit ejecuta todo el código de arriba a abajo
        - El número aleatorio se muestra correctamente
        - El formulario funciona normalmente
        
        **Con `stop()` activado:**
        - Streamlit detiene la ejecución en el punto del `st.stop()`
        - Nada después de esa línea se ejecuta
        - La aplicación parece "congelada" en ese estado
        """)

with col2:
    st.header("🔄 Función: `st.rerun()`")
    st.markdown("""
    **`st.rerun()`** reinicia la ejecución de la aplicación desde el principio.
    
    - La aplicación se vuelve a ejecutar completamente
    - Los valores en `st.session_state` se preservan
    - Generamos números aleatorios como demostración de acceso a datos dinámicos
    - Útil para actualizar la aplicación después de cambios
    """)
    
    st.divider()
    
    # Demostración de st.rerun()
    st.subheader("Demo: Efecto de `rerun()`")
    
    # Contador de reruns
    st.metric(label="Veces que se ha hecho rerun", value=st.session_state.contador_rerun)
    
    # Historial de números aleatorios
    st.markdown(f"**Historial de números aleatorios:** {', '.join(map(str, st.session_state.historial_numeros[-5:]))}")
    
    # Botón para rerun
    if st.button("🔄 Ejecutar rerun()", type="primary"):
        st.session_state.contador_rerun += 1
        # Generar nuevo número aleatorio
        nuevo_numero = random.randint(1, 100)
        st.session_state.numero_aleatorio = nuevo_numero
        st.session_state.historial_numeros.append(nuevo_numero)
        # Limitar el historial a los últimos 10 valores
        if len(st.session_state.historial_numeros) > 10:
            st.session_state.historial_numeros = st.session_state.historial_numeros[-10:]
        
        st.success(f"✅ rerun() ejecutado. Nuevo número: {nuevo_numero}")
        # Pequeña pausa para que el usuario vea el mensaje
        time.sleep(0.5)
        st.rerun()  # Reinicia la aplicación desde el principio
    
    # Explicación de lo que sucede con rerun()
    with st.expander("📖 ¿Qué está pasando aquí?"):
        st.markdown("""
        **Cuando haces clic en el botón:**
        1. Se incrementa el contador de reruns
        2. Se genera un nuevo número aleatorio
        3. Se actualiza el historial de números
        4. `st.rerun()` reinicia la aplicación desde el principio
        5. La página se recarga y se muestran los nuevos valores
        
        **Nota:** Los valores en `st.session_state` se preservan entre reruns, 
        por eso el contador y el historial mantienen sus valores.
        """)

# Sección común para ambos ejemplos
st.divider()
st.header("📝 Ejemplo práctico: Formulario")

# Formulario para mostrar que con stop() no funciona
with st.form(key='formulario_demo'):
    st.markdown("Este formulario muestra cómo `stop()` afecta la interactividad:")
    st.markdown("Tenemos un botón que genera un número aleatorio nuevo. Los elementos de " \
    "la página se actualizan teniendo en cuenta el nuevo número generado ya que el botón hace un rerun " \
    "automático. No es necesario que hagamos la ejecución de `rerun()` de manera explícita. " \
    "Ejecutaremos el `rerun()` de manera explícita cuando el refresco deba hacerse sin que lo solicite el usuario.")
    texto_input = st.text_input(
        label='Introduce un texto:',
        value=st.session_state.texto_guardado,
        placeholder="Escribe algo aquí..."
    )
    
    col_form1, col_form2, col_form3 = st.columns(3)
    
    with col_form1:
        submit_button = st.form_submit_button(label='Guardar texto')
    
    with col_form2:
        # Botón para limpiar el texto guardado
        if st.form_submit_button("Limpiar texto"):
            st.session_state.texto_guardado = ""
            st.rerun()
    
    with col_form3:
        # Botón para generar nuevo número aleatorio sin rerun
        if st.form_submit_button("Nuevo número (sin rerun)"):
            st.session_state.numero_aleatorio = random.randint(1, 100)
            st.session_state.historial_numeros.append(st.session_state.numero_aleatorio)

if submit_button and texto_input:
    st.session_state.texto_guardado = texto_input
    st.success(f"✅ Texto guardado: '{texto_input}'")
    # Nota: En un caso real, aquí podríamos hacer st.rerun() para actualizar
    # pero lo omitimos para mostrar la diferencia

# Mostrar texto guardado si existe
if st.session_state.texto_guardado:
    st.info(f"📝 **Texto actualmente guardado:** '{st.session_state.texto_guardado}'")

# Comparación final
st.divider()
st.header("📊 Resumen comparativo")

comparison_col1, comparison_col2 = st.columns(2)

with comparison_col1:
    st.subheader("⏸️ `st.stop()`")
    st.markdown("""
    - **Efecto:** Detiene la ejecución
    - **Líneas de código a continuación:** No se ejecutan
    - **Estado:** Se congela
    - **Interactividad:** Limitada después del punto de stop
    - **Caso de uso:** Detener la app cuando falta información crítica
    """)

with comparison_col2:
    st.subheader("🔄 `st.rerun()`")
    st.markdown("""
    - **Efecto:** Reinicia la ejecución
    - **Líneas de código a continuación:** Se ejecutan tras el reinicio
    - **Estado:** Se preserva en session_state
    - **Interactividad:** Total después del rerun
    - **Caso de uso:** Actualizar la app tras cambios importantes
    """)

# Nota final
st.info("💡 **Consejo:** Usa `st.stop()` para condiciones de error o cuando falten datos esenciales. Usa `st.rerun()` cuando necesites refrescar completamente la aplicación después de una acción del usuario.")

# Código de ejemplo (opcional)
with st.expander("👨‍💻 Ver código fuente de esta demo"):
    st.code('''
import streamlit as st
import random
import time

# Configuración de la página
st.set_page_config(page_title="Demo: stop() vs rerun()", page_icon="⏸️🔄", layout="wide")

# Inicialización del estado de sesión
if 'contador_rerun' not in st.session_state:
    st.session_state.contador_rerun = 0
if 'numero_aleatorio' not in st.session_state:
    st.session_state.numero_aleatorio = random.randint(1, 100)
if 'historial_numeros' not in st.session_state:
    st.session_state.historial_numeros = [st.session_state.numero_aleatorio]
if 'texto_guardado' not in st.session_state:
    st.session_state.texto_guardado = ""

# Título y descripción
st.title("⏸️🔄 Demostración: stop() vs rerun() en Streamlit")
st.markdown("""
Esta aplicación muestra la diferencia fundamental entre dos funciones de control de flujo en Streamlit:
`st.stop()` y `st.rerun()`. Ambas afectan la ejecución de la aplicación, pero de maneras muy diferentes.
""")

# Crear columnas para organizar el contenido
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.header("⏸️ Función: `st.stop()`")
    st.markdown("""
    **`st.stop()`** detiene inmediatamente la ejecución de la aplicación en ese punto.
    
    - Todo el código que venga después de `st.stop()` **NO se ejecutará**
    - La aplicación se "congela" en el estado actual
    - No se pueden actualizar widgets después del punto de detención
    - Para continuar, el usuario debe desactivar la condición que causó el `stop()`
    """)
    
    st.divider()
    
    # Demostración de st.stop()
    st.subheader("Demo: Efecto de `stop()`")
    
    st.markdown("Marca la casilla a continuación para activar `st.stop()`:")
    
    # Checkbox para activar stop()
    if st.checkbox("Activar stop()", key="stop_checkbox"):
        st.warning("¡stop() activado! La ejecución se detendrá aquí.")
        st.info("""
        **Observa que:**
        1. El número aleatorio NO se regenera
        2. El formulario de abajo NO se puede usar
        3. El contador NO se actualiza
        """)
        st.stop()  # ¡La ejecución se detiene aquí!
    
    # Código después de stop() - solo se ejecuta si stop() no se activó
    st.success("✅ `stop()` NO está activado. Todo el código después se ejecuta normalmente.")
    
    # Mostrar número aleatorio actual
    st.metric(label="Número aleatorio actual", value=st.session_state.numero_aleatorio)
    
    # Explicación de lo que sucede con stop()
    with st.expander("📖 ¿Qué está pasando aquí?"):
        st.markdown("""
        **Sin `stop()` activado:**
        - Streamlit ejecuta todo el código de arriba a abajo
        - El número aleatorio se muestra correctamente
        - El formulario funciona normalmente
        
        **Con `stop()` activado:**
        - Streamlit detiene la ejecución en el punto del `st.stop()`
        - Nada después de esa línea se ejecuta
        - La aplicación parece "congelada" en ese estado
        """)

with col2:
    st.header("🔄 Función: `st.rerun()`")
    st.markdown("""
    **`st.rerun()`** reinicia la ejecución de la aplicación desde el principio.
    
    - La aplicación se vuelve a ejecutar completamente
    - Los valores en `st.session_state` se preservan
    - Generamos números aleatorios como demostración de acceso a datos dinámicos
    - Útil para actualizar la aplicación después de cambios
    """)
    
    st.divider()
    
    # Demostración de st.rerun()
    st.subheader("Demo: Efecto de `rerun()`")
    
    # Contador de reruns
    st.metric(label="Veces que se ha hecho rerun", value=st.session_state.contador_rerun)
    
    # Historial de números aleatorios
    st.markdown(f"**Historial de números aleatorios:** {', '.join(map(str, st.session_state.historial_numeros[-5:]))}")
    
    # Botón para rerun
    if st.button("🔄 Ejecutar rerun()", type="primary"):
        st.session_state.contador_rerun += 1
        # Generar nuevo número aleatorio
        nuevo_numero = random.randint(1, 100)
        st.session_state.numero_aleatorio = nuevo_numero
        st.session_state.historial_numeros.append(nuevo_numero)
        # Limitar el historial a los últimos 10 valores
        if len(st.session_state.historial_numeros) > 10:
            st.session_state.historial_numeros = st.session_state.historial_numeros[-10:]
        
        st.success(f"✅ rerun() ejecutado. Nuevo número: {nuevo_numero}")
        # Pequeña pausa para que el usuario vea el mensaje
        time.sleep(0.5)
        st.rerun()  # Reinicia la aplicación desde el principio
    
    # Explicación de lo que sucede con rerun()
    with st.expander("📖 ¿Qué está pasando aquí?"):
        st.markdown("""
        **Cuando haces clic en el botón:**
        1. Se incrementa el contador de reruns
        2. Se genera un nuevo número aleatorio
        3. Se actualiza el historial de números
        4. `st.rerun()` reinicia la aplicación desde el principio
        5. La página se recarga y se muestran los nuevos valores
        
        **Nota:** Los valores en `st.session_state` se preservan entre reruns, 
        por eso el contador y el historial mantienen sus valores.
        """)

# Sección común para ambos ejemplos
st.divider()
st.header("📝 Ejemplo práctico: Formulario")

# Formulario para mostrar que con stop() no funciona
with st.form(key='formulario_demo'):
    st.markdown("Este formulario muestra cómo `stop()` afecta la interactividad:")
    st.markdown("Tenemos un botón que genera un número aleatorio nuevo. Los elementos de " \
    "la página se actualizan teniendo en cuenta el nuevo número generado ya que el botón hace un rerun " \
    "automático. No es necesario que hagamos la ejecución de `rerun()` de manera explícita. " \
    "Ejecutaremos el `rerun()` de manera explícita cuando el refresco deba hacerse sin que lo solicite el usuario.")
    texto_input = st.text_input(
        label='Introduce un texto:',
        value=st.session_state.texto_guardado,
        placeholder="Escribe algo aquí..."
    )
    
    col_form1, col_form2, col_form3 = st.columns(3)
    
    with col_form1:
        submit_button = st.form_submit_button(label='Guardar texto')
    
    with col_form2:
        # Botón para limpiar el texto guardado
        if st.form_submit_button("Limpiar texto"):
            st.session_state.texto_guardado = ""
            st.rerun()
    
    with col_form3:
        # Botón para generar nuevo número aleatorio sin rerun
        if st.form_submit_button("Nuevo número (sin rerun)"):
            st.session_state.numero_aleatorio = random.randint(1, 100)
            st.session_state.historial_numeros.append(st.session_state.numero_aleatorio)

if submit_button and texto_input:
    st.session_state.texto_guardado = texto_input
    st.success(f"✅ Texto guardado: '{texto_input}'")
    # Nota: En un caso real, aquí podríamos hacer st.rerun() para actualizar
    # pero lo omitimos para mostrar la diferencia

# Mostrar texto guardado si existe
if st.session_state.texto_guardado:
    st.info(f"📝 **Texto actualmente guardado:** '{st.session_state.texto_guardado}'")

# Comparación final
st.divider()
st.header("📊 Resumen comparativo")

comparison_col1, comparison_col2 = st.columns(2)

with comparison_col1:
    st.subheader("⏸️ `st.stop()`")
    st.markdown("""
    - **Efecto:** Detiene la ejecución
    - **Líneas de código a continuación:** No se ejecutan
    - **Estado:** Se congela
    - **Interactividad:** Limitada después del punto de stop
    - **Caso de uso:** Detener la app cuando falta información crítica
    """)

with comparison_col2:
    st.subheader("🔄 `st.rerun()`")
    st.markdown("""
    - **Efecto:** Reinicia la ejecución
    - **Líneas de código a continuación:** Se ejecutan tras el reinicio
    - **Estado:** Se preserva en session_state
    - **Interactividad:** Total después del rerun
    - **Caso de uso:** Actualizar la app tras cambios importantes
    """)

# Nota final
st.info("💡 **Consejo:** Usa `st.stop()` para condiciones de error o cuando falten datos esenciales. Usa `st.rerun()` cuando necesites refrescar completamente la aplicación después de una acción del usuario.")
            
''', language="python")