import streamlit as st
import pandas as pd

# Set the truck and transport theme using emojis
st.set_page_config(page_title="Rate Review Calculator 2024 🚛", page_icon="🚚")

# Title and description with the truck theme
st.title("🚛 Truck & Transport Rate Review Calculator 2024 🚛")
st.write("Calculate your rates and transport costs with our interactive calculator!")

# Load the Excel file
uploaded_file = 'Rate review Calculator 2024.xlsx'  # Adjust the file path as needed

# Check if file is successfully loaded
try:
    # Load the Excel file and display all three pages (sheets)
    excel_file = pd.ExcelFile(uploaded_file)
    st.write("### Available Sheets in the Excel File:")
    st.write(excel_file.sheet_names)

    # Display and review all three sheets
    for sheet in excel_file.sheet_names:
        df = pd.read_excel(uploaded_file, sheet_name=sheet)
        st.write(f"### Preview of {sheet} Sheet")
        st.dataframe(df)

    # User inputs: Confirm or change the required values for calculation
    st.write("### Enter the required data to calculate the values:")

    # Ask user to input/confirm values from the Excel sheet (adjust based on the actual structure)
    weight = st.number_input("Enter the weight (kg):", min_value=0.0, value=1000.0)
    distance = st.number_input("Enter the distance (km):", min_value=0.0, value=500.0)
    fuel_cost = st.number_input("Enter the fuel cost per liter:", min_value=0.0, value=15.0)
    rate_per_km = st.number_input("Enter the rate per kilometer:", min_value=0.0, value=10.0)

    # Calculate based on inputs
    total_rate = weight * distance * rate_per_km
    total_fuel_cost = (distance / 4) * fuel_cost  # Assuming fuel consumption is 4km per liter

    # Display calculated values
    st.write(f"### Total Transport Rate: {total_rate}")
    st.write(f"### Total Fuel Cost: {total_fuel_cost}")

    # Option to download the updated Excel file with these values
    if st.button('Download Updated Rates'):
        # Load the first sheet (or the relevant sheet for editing) and update it with new calculated values
        df_update = pd.read_excel(uploaded_file, sheet_name=excel_file.sheet_names[0])
        df_update.loc[0, 'Total Rate'] = total_rate
        df_update.loc[0, 'Fuel Cost'] = total_fuel_cost

        # Save the updated Excel file
        df_update.to_excel('Updated_Rate_Calculator.xlsx', index=False)
        with open('Updated_Rate_Calculator.xlsx', 'rb') as file:
            st.download_button('Download Updated Excel', file, file_name='Updated_Rate_Calculator.xlsx')

    # Fun and engaging transport-themed messages
    st.markdown("### Keep on trucking with accurate rate reviews! 🚚💨")
    st.write("Make sure your transport costs are always in check!")

except FileNotFoundError:
    st.error("The file 'Rate review Calculator 2024.xlsx' was not found. Please check the file path.")
except Exception as e:
    st.error(f"An error occurred: {e}")
