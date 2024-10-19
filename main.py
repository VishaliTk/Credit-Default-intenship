
import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model
with open('credit_default_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app interface
st.title('Credit Card Default Prediction')
