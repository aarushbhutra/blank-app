import streamlit as st
import pandas as pd

# Load the Excel file
file_path = 'icl.xlsx'

# Load the Excel file with Pandas
@st.cache_data
def load_data(sheet_name=None):
    return pd.read_excel(file_path, sheet_name=sheet_name)

# Sidebar to select a sheet
sheet_names = pd.ExcelFile(file_path).sheet_names
selected_sheet = st.sidebar.selectbox('Select a sheet', sheet_names)

# Display the selected sheet's data
data = load_data(sheet_name=selected_sheet)
st.write(f"## Displaying data from: {selected_sheet}")
st.dataframe(data)

# Option to download data as CSV
csv = data.to_csv(index=False)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name=f"{selected_sheet}_data.csv",
    mime='text/csv',
)

# Option to display summary statistics
if st.checkbox("Show summary statistics"):
    st.write(data.describe())
