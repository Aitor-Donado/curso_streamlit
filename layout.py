import numpy as np
import streamlit as st

# App title
st.title("Streamlit Custom Theme Demo")
# Display text with different formatting
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is some text.")
st.write("This Streamlit app demonstrates the customtheme.")
# Sidebar with some widgets
st.sidebar.header("Sidebar")
st.sidebar.write("This is the sidebar.")
st.sidebar.checkbox("Check me out")
st.sidebar.radio("Choose an option", ['Option 1','Option 2', 'Option 3'])
st.sidebar.selectbox("Select a number", np.arange(1,11))