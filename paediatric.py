import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data (replace with your actual dataset)
data = {
    'child_sex': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'age_recorded': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'age_years': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'weight': [5, 8, 10, 11, 13, 15, 17, 20, 25, 38],
    'fever': [1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
    'rtss_1': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'temp': [35, 36, 37, 38, 39, 38, 37, 37, 40, 41],
    'mal1_order': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'mal1_rapid_result': [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    'arte_pres': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'coart1_pres': [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    'hb1_result': [1, 2, 3, 4, 5, 8, 9, 10, 12, 16],
    'outcome': ['Died', 'Alive', 'Alive', 'Died', 'Alive', 'Died', 'Alive', 'Died', 'Alive', 'Alive']
}
df = pd.DataFrame(data)

# Correct the child_sex and outcome mappings
df['child_sex'] = df['child_sex'].map({'M': 1, 'F': 0})
df['outcome'] = df['outcome'].map({'Died': 0, 'Alive': 1})

# Prepare data
X = df[['child_sex', 'age_recorded', 'age_years', 'weight', 'fever', 'rtss_1', 'temp', 'mal1_order', 'mal1_rapid_result', 'arte_pres', 'coart1_pres', 'hb1_result']]
y = df['outcome']

# Standardize the data (this must be done the same way during prediction)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Load the trained model using joblib
model = joblib.load('paediatric_model.joblib')  # Load the model

# Streamlit app layout
st.title('Mortality Prediction Model')

# Collect user input
child_sex = st.selectbox('Child Sex (0 for Female, 1 for Male)', [0, 1])
age_recorded = st.number_input('Age Recorded')
age_years = st.number_input('Age (in Years)')
weight = st.number_input('Weight')
fever = st.selectbox('Fever (1 if Yes, 0 if No)', [0, 1])
rtss_1 = st.number_input('RTSS 1 Result (0 or 1)')
temp = st.number_input('Temperature')
mal1_order = st.number_input('Malaria Order (1 or 0)')
mal1_rapid_result = st.selectbox('Malaria Rapid Result (0 for Negative, 1 for Positive)', [0, 1])
arte_pres = st.selectbox('Arte Medication Present (0 for No, 1 for Yes)', [0, 1])
coart1_pres = st.selectbox('Coart Medication Present (0 for No, 1 for Yes)', [0, 1])
hb1_result = st.number_input('Hemoglobin Result')

# When the user clicks "Predict Outcome"
if st.button('Predict Outcome'):
    # Prepare input data for prediction
    input_data = pd.DataFrame({
        'child_sex': [child_sex],
        'age_recorded': [age_recorded],
        'age_years': [age_years],  # Ensure exact match in feature names
        'weight': [weight],
        'fever': [fever],
        'rtss_1': [rtss_1],
        'temp': [temp],
        'mal1_order': [mal1_order],
        'mal1_rapid_result': [mal1_rapid_result],
        'arte_pres': [arte_pres],
        'coart1_pres': [coart1_pres],
        'hb1_result': [hb1_result],
    })
    
    # Standardize the input data (ensure it's scaled the same way as training)
    input_scaled = scaler.transform(input_data)
    
    # Predict outcome using the loaded model
    prediction = model.predict(input_scaled)[0]

    # Add error handling in case prediction is not 0 or 1
    outcome_map = {2: 'Died', 1: 'Alive'}
    
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("Predicted Outcome: **Alive**")
    else:
        st.error("Predicted Outcome: **Dead**")
