import streamlit as st
# Creating a text input widget
text = st.text_input(key="text_input", label = "Enter text")
# Incorrect way: Attempting to modify the widget value after creation
st.session_state.text_input = "New Value"
# This will raise StreamlitAPIException