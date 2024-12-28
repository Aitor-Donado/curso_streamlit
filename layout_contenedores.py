import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Titlest.title('Streamlit App With Layouts and Containers')
# Using columns for input fields
# Title
st.title('App Streamlit Con Layouts ni Containers')
col1, col2 = st.columns(2)
with col1:
    user_input = st.text_input("Enter some text")
with col2:
    number_input = st.number_input("Enter a number")
# Button in its own container
with st.container():
    if st.button('Click Me'):
        st.write('Button clicked!')

# Plotting a simple line chart in an expander
with st.expander("See Chart"):
    data = pd.DataFrame(np.random.randn(20, 2),
columns=['A', 'B'])
st.line_chart(data)
# Footer text in a container
with st.container():
    st.write("Here's some organized text below the chart.")