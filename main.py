
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



    
