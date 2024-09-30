import streamlit as st
import pandas as pd

# Streamlit app layout
st.title('Mortality Prediction Model')

# Collect user input
child_sex = st.selectbox('Child Sex (0 for Female, 1 for Male)', [0, 1])
age_recorded = st.number_input('Age Recorded', min_value=0)
age_years = st.number_input('Age (in Years)', min_value=0)
weight = st.number_input('Weight', min_value=0)
fever = st.selectbox('Fever (1 if Yes, 0 if No)', [0, 1])
rtss_1 = st.number_input('RTSS 1 Result (0 or 1)', min_value=0, max_value=1)
temp = st.number_input('Temperature', min_value=0.0)
mal1_order = st.number_input('Malaria Order (1 or 0)', min_value=0, max_value=1)
mal1_rapid_result = st.selectbox('Malaria Rapid Result (0 for Negative, 1 for Positive)', [0, 1])
arte_pres = st.selectbox('Arte Medication Present (0 for No, 1 for Yes)', [0, 1])
coart1_pres = st.selectbox('Coart Medication Present (0 for No, 1 for Yes)', [0, 1])
hb1_result = st.number_input('Hemoglobin Result', min_value=0)

# When the user clicks "Predict Outcome"
if st.button('Predict Outcome'):
    # Predict outcome based on child sex
    if child_sex == 1:  # Male
        st.success("Predicted Outcome: **Alive**")
    else:  # Female
        st.error("Predicted Outcome: **Dead**")
