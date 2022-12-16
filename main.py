import json
import requests
import streamlit as st

url = "https://api-test-drive.onrender.com/diabetes_prediction"

def main():

    ## app title
    st.title("Diabetes Prediction Webapp")
    col1, col2, col3 = st.columns(3)

    ## input data
    with col1:
        pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        glucose = st.text_input("Glucose Level")
    with col3:
        bloodPressure = st.text_input("Blood Pressure value")
    with col1:
        skinThickness = st.text_input("Skin Thickness value")
    with col2:
        insulin = st.text_input("Insulin level value")
    with col3:
        bmi = st.text_input("BMI value")
    with col1:
        diabetesPedigree = st.text_input("Diabetes Pedigree function value")
    with col2:
        age = st.text_input("Age of the person")

    ## prediction
    diagnosis = ''

    ## creating button for prediction
    if st.button('Diabetes Test Result'):
        input_data_for_model = {
            'Pregnancies': pregnancies,
            'Glucose': glucose,
            'BloodPressure': bloodPressure,
            'SkinThickness': skinThickness,
            'Insulin': insulin,
            'BMI': bmi,
            'DiabetesPedigreeFunction': diabetesPedigree,
            'Age': age
        }

        input_json = json.dumps(input_data_for_model)

        response = requests.post(url, data=input_json)
        diagnosis = response.text
    st.success(diagnosis)

if __name__ == '__main__':
    main()