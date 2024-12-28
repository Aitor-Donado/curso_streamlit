import streamlit as st
# Setting the page config
st.set_page_config(page_title="Mi mejor App",
    page_icon=":tada:",
    layout="wide")
# Displaying code and its output
with st.echo():
    # This code will be shown and executed
    st.write("Esta línea de código se mostrará y después se ejecutará.")

# Showing help information for a Streamlit function
st.help(st.sidebar)