import streamlit as st
import pandas as pd

# Truck and transport theme using emojis
st.set_page_config(page_title="Rate Review Calculator 2024 🚛", page_icon="🚚")

# Title and description with the truck theme
st.title("🚛 Truck & Transport Rate Review Calculator 2024 🚛")
st.write("Calculate your rates and transport costs with our exciting, truck-themed calculator!")

# Load the Excel file
uploaded_file = 'Rate review Calculator 2024.xlsx'
df = pd.read_excel(uploaded_file)

# Display the Excel data for user review
st.write("### Rate Data Preview")
st.dataframe(df)

# User input: Total amount for rate calculation
total_amount = st.number_input("Enter the total amount for calculation", min_value=0.0)

# If an amount is entered, calculate the values based on percentage
if total_amount > 0:
    df['Calculated Rate'] = df['Percentage'] / 100 * total_amount
    st.write("### Calculated Rate Based on Input Amount")
    st.dataframe(df[['Description', 'Percentage', 'Calculated Rate']])

# Option to download the updated Excel file with calculated rates
if st.button('Download Updated Rates'):
    df.to_excel('Updated_Rate_Calculator.xlsx', index=False)
    with open('Updated_Rate_Calculator.xlsx', 'rb') as file:
        st.download_button('Download Updated Excel', file, file_name='Updated_Rate_Calculator.xlsx')

# Fun and engaging transport-themed messages
st.markdown("### Keep on trucking with accurate rate reviews! 🚚💨")
st.write("Make sure your transport costs are always in check!")
