import streamlit as st
# on_change event in a text input widget
def handle_text_change():
    st.write("Text has changed")

st.text_input("Change the text", on_change=handle_text_change)
# on_click event in a button widget
st.button("Click me", on_click=lambda: st.write("Button clicked"))