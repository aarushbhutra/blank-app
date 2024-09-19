import streamlit as st
import pandas as pd

# Load the CSV file
file_path = 'icl.csv'

@st.cache_data
def load_data():
    return pd.read_csv(file_path)

# Load the data
data = load_data()

# Display the data in Streamlit
st.title("UG Admissions Statistics (2019-2023)")
st.write("Displaying data from the uploaded CSV file:")

# Show the data in a dataframe
st.dataframe(data)

# Option to display summary statistics
if st.checkbox("Show summary statistics"):
    st.write(data.describe())
