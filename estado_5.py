import streamlit as st
# Incorrect way: Attempting to set the state of a button
st.session_state.my_button = True
# Not allowed
# Using a button
if st.button("Click me", key = 'my_button'):
    st.write("Button was clicked!")