import streamlit as st

st.title("Carga de archivos")
extensiones_admitidas = ["jpg", "png", "bmp"]

st.markdown("## Carga una imagen cada vez")

imagen = st.file_uploader("Carga una imagen", type=extensiones_admitidas)
if imagen:
		st.image(imagen)

st.markdown("---")
st.markdown("## Carga varias imagenes cada vez")		

imagenes = st.file_uploader("Carga las imágenes", 
		type=extensiones_admitidas, 
		accept_multiple_files=True)
if imagenes:
		for imagen in imagenes:
			st.image(imagen)