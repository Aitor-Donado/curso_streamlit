import streamlit as st
# Incorrect way: Setting state via Session State API and value parameter
st.session_state.text_input = "New Value"
# Creating a text input widget
text = st.text_input(key="text_input", 
                     label = "Enter text" , 
                     value = st.session_state.text_input)