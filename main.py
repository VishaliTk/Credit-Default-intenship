
import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open('credit_default_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


# Streamlit app interface
st.title('Credit Card Default Prediction')

# Collect user input
LIMIT_BAL = st.number_input('Enter Credit Limit Balance:', min_value=0.0, step=1000.0)
SEX = st.selectbox('Select Gender (1 = Male, 2 = Female):', [1, 2])
EDUCATION = st.selectbox('Select Education (1 = Graduate, 2 = University, 3 = High School, 4 = Others):', [1, 2, 3, 4])
MARRIAGE = st.selectbox('Select Marital Status (1 = Married, 2 = Single, 3 = Others):', [1, 2, 3])
AGE = st.number_input('Enter Age:', min_value=18, step=1)
PAY_SEPT = st.number_input('Enter Repayment Status in September:', step=1)
PAY_AUG = st.number_input('Enter Repayment Status in August:', step=1)
PAY_JUL = st.number_input('Enter Repayment Status in July:', step=1)
PAY_JUN = st.number_input('Enter Repayment Status in June:', step=1)
PAY_MAY = st.number_input('Enter Repayment Status in May:', step=1)
PAY_APR = st.number_input('Enter Repayment Status in April:', step=1)
BILL_AMT_SEPT = st.number_input('Enter Bill Amount in September:', step=1000.0)
BILL_AMT_AUG = st.number_input('Enter Bill Amount in August:', step=1000.0)
BILL_AMT_JUL = st.number_input('Enter Bill Amount in July:', step=1000.0)
BILL_AMT_JUN = st.number_input('Enter Bill Amount in June:', step=1000.0)
BILL_AMT_MAY = st.number_input('Enter Bill Amount in May:', step=1000.0)
BILL_AMT_APR = st.number_input('Enter Bill Amount in April:', step=1000.0)
PAY_AMT_SEPT = st.number_input('Enter Payment Amount in September:', step=100.0)
PAY_AMT_AUG = st.number_input('Enter Payment Amount in August:', step=100.0)
PAY_AMT_JUL = st.number_input('Enter Payment Amount in July:', step=100.0)
PAY_AMT_JUN = st.number_input('Enter Payment Amount in June:', step=100.0)
PAY_AMT_MAY = st.number_input('Enter Payment Amount in May:', step=100.0)
PAY_AMT_APR = st.number_input('Enter Payment Amount in April:', step=100.0)
