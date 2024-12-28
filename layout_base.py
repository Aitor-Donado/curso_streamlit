import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Title
st.title('App Streamlit Sin Layouts ni Containers')
# User Input
user_input = st.text_input("Enter some text")
number_input = st.number_input("Enter a number")
# Button
if st.button('Click Me'):
    st.write('Button clicked!')
# Plotting a simple line chart
data = pd.DataFrame(np.random.randn(20, 2), columns=['A', 'B'])
st.line_chart(data)
# Displaying some textst.write("Here's some text below the chart.")