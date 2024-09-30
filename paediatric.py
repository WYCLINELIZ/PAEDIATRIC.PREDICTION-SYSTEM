import streamlit as st
import pandas as pd

# Streamlit app layout
st.title('Mortality Prediction Model')

# Collect user input
child_sex = st.selectbox('Child Sex (0 for Female, 1 for Male)', [0, 1])
age_recorded = st.text_input('Age Recorded (in years)', '0')
age_years = st.text_input('Age (in Years)', '0')
weight = st.text_input('Weight (in kg)', '0')
fever = st.selectbox('Fever (1 if Yes, 0 if No)', [0, 1])
rtss_1 = st.text_input('RTSS 1 Result (0 or 1)', '0')
temp = st.text_input('Temperature (°C)', '0')
mal1_order = st.selectbox('Malaria Order (1 for Positive, 0 for Negative)', [0, 1])
mal1_rapid_result = st.selectbox('Malaria Rapid Result (0 for Negative, 1 for Positive)', [0, 1])
arte_pres = st.selectbox('Arte Medication Present (0 for No, 1 for Yes)', [0, 1])
coart1_pres = st.selectbox('Coart Medication Present (0 for No, 1 for Yes)', [0, 1])
hb1_result = st.text_input('Hemoglobin Result', '0')

# When the user clicks "Predict Outcome"
if st.button('Predict Outcome'):
    # Convert input data to appropriate types
    try:
        age_recorded = int(age_recorded)
        age_years = int(age_years)
        weight = float(weight)
        rtss_1 = int(rtss_1)
        temp = float(temp)
        hb1_result = float(hb1_result)

        # Predict outcome based on child sex and other conditions
        if child_sex == 1 and fever == 1:  # Male and has fever
            prediction = "Alive"
        elif child_sex == 0 and fever == 0:  # Female and no fever
            prediction = "Dead"
        else:
            prediction = "Prediction may vary based on other clinical factors."

        st.success(f"Predicted Outcome: **{prediction}**")

        # Display all input values for reference in a dialog-like box
        with st.expander("View Input Data", expanded=True):
            input_data = {
                'Child Sex': "Male" if child_sex == 1 else "Female",
                'Age Recorded': age_recorded,
                'Age (Years)': age_years,
                'Weight (kg)': weight,
                'Fever': "Yes" if fever == 1 else "No",
                'RTSS 1 Result': rtss_1,
                'Temperature (°C)': temp,
                'Malaria Order': "Positive" if mal1_order == 1 else "Negative",
                'Malaria Rapid Result': "Positive" if mal1_rapid_result == 1 else "Negative",
                'Arte Medication Present': "Yes" if arte_pres == 1 else "No",
                'Coart Medication Present': "Yes" if coart1_pres == 1 else "No",
                'Hemoglobin Result': hb1_result
            }

            # Format the output in a string
            input_data_str = "\n".join([f"{key}: {value}" for key, value in input_data.items()])
            st.text_area("Entered Input Data", input_data_str, height=250)

    except ValueError:
        st.error("Please enter valid numerical values for age, weight, temperature, and hemoglobin result.")
