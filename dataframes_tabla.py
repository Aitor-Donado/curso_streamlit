import pandas as pd
import streamlit as st

# En el archivo dataframes_tabla.py
df = pd.DataFrame([
	{"command": "st.selectbox", "rating": 4, "is_widget": True},
	{"command": "st.balloons", "rating": 5, "is_widget": False},
	{"command": "st.time_input", "rating": 3, "is_widget": True}])

# Vista estática del dataframe.
st.write("DataFrame visto con st.table")
st.table(df)
st.divider()

# Vista formateada del dataframe. Puede descargarse.
st.write("DataFrame visto con st.dataframe")
st.dataframe(df)
st.divider()

# Con data_editor se puede editar el contenido y extraer el valor modificado.
st.write("DataFrame visto y editable con st.data_editor")
edited_df = st.data_editor(df, num_rows="dynamic")
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}**")