import streamlit as st
import pandas as pd
import os

# CSV file path
csv_file = 'options_data.csv'

# Function to write selection to CSV
def write_to_csv(selection):
    # Check if CSV exists
    if os.path.exists(csv_file):
        # Read the existing data
        df = pd.read_csv(csv_file)
    else:
        # Create an empty dataframe with columns if CSV does not exist
        df = pd.DataFrame(columns=['Selection'])
    
    # Append the new selection
    new_data = pd.DataFrame({'Selection': [selection]})
    df = pd.concat([df, new_data], ignore_index=True)
    
    # Write the updated dataframe to CSV
    df.to_csv(csv_file, index=False)

# Streamlit app title
st.title('Choose an Option')

# Option selection using radio buttons
option = st.radio("Select an option:", ['A', 'B', 'C', 'D'])

# Button to submit the selection
if st.button('Submit'):
    write_to_csv(option)
    st.success(f"You selected option {option}. The data has been saved.")
    
# Show current data in CSV file
if os.path.exists(csv_file):
    st.write('Current Data in CSV:')
    df = pd.read_csv(csv_file)
    st.dataframe(df)
else:
    st.write('No data found yet.')
