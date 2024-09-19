import streamlit as st
import pandas as pd

# Load the Excel file with pyarrow as engine
file_path = 'icl.xlsx'

@st.cache_data
def load_data():
    return pd.read_excel(file_path, engine='pyarrow')

# Load the data
data = load_data()

# Display the data in Streamlit
st.title("UG Admissions Statistics (2019-2023)")
st.write("Displaying data from the uploaded Excel file:")

# Show the data in a dataframe
st.dataframe(data)

# Option to display summary statistics
if st.checkbox("Show summary statistics"):
    st.write(data.describe())
