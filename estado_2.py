import streamlit as st
# Evento on_change en un text_input
def handle_text_change():
    st.write("Text has changed")

st.text_input("Change the text", on_change=handle_text_change)
# Evento on_click en un button
st.button("Click me", on_click=lambda: st.write("Button clicked"))