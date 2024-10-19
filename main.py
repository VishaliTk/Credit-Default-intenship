
import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open('credit_default_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)


# Streamlit app interface
st.title('Credit Card Default Prediction')

# Collect user input
LIMIT_BAL = st.number_input('Enter Credit Limit Balance:', min_value=0.0, step=1000.0)
AGE = st.number_input('Enter Age:', min_value=18, step=1)
BILL_AMT_SEPT = st.number_input('Enter Bill Amount in September:', step=1000.0)
BILL_AMT_AUG = st.number_input('Enter Bill Amount in August:', step=1000.0)
PAY_SEPT = st.number_input('Enter Repayment Status in September:', step=1)

# Ensure no input is left undefined
if st.button('Predict Default'):
    # Create input array for prediction using only the selected features
    input_data = np.array([[LIMIT_BAL, AGE, BILL_AMT_SEPT, BILL_AMT_AUG, PAY_SEPT]])

    # Scale the input data using the loaded scaler
    input_data_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_data_scaled)
    
    # Display the prediction result
    if prediction[0] == 1:
        st.write('The customer is likely to default on the credit card payment.')
    else:
        st.write('The customer is not likely to default on the credit card payment.')


    
