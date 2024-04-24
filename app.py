import streamlit as st
import joblib
import pandas as pd
import os

print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())

# Load the trained model
model = joblib.load('rf_model.pkl')

# Function to predict stroke
def predict_stroke(data):
    prediction = model.predict(data)
    return prediction

def main():
    # Title
    st.title('Stroke Prediction App')

    # Sidebar
    st.sidebar.title('User Input Features')
    
    # Creating input features
    age = st.sidebar.slider('Age', 0, 100, 50)
    hypertension = st.sidebar.selectbox('Hypertension', [0, 1])
    heart_disease = st.sidebar.selectbox('Heart Disease', [0, 1])
    avg_glucose_level = st.sidebar.number_input('Average Glucose Level')
    bmi = st.sidebar.number_input('BMI')
    gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
    gender_male = 1 if gender == 'Male' else 0
    ever_married = st.sidebar.selectbox('Ever Married', ['Yes', 'No'])
    ever_married_yes = 1 if ever_married == 'Yes' else 0
    work_type = st.sidebar.selectbox('Work Type', ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
    Residence_type = st.sidebar.selectbox('Residence Type', ['Urban', 'Rural'])

    # Mapping work_type and Residence_type to binary values
    work_type_mapping = {'Private': 0, 'Self-employed': 1, 'Govt_job': 2, 'children': 3, 'Never_worked': 4}
    residence_mapping = {'Urban': 0, 'Rural': 1}
    work_type_encoded = work_type_mapping[work_type]
    residence_encoded = residence_mapping[Residence_type]

    # Creating dataframe with input features
    input_data = pd.DataFrame({'age': [age],
                               'hypertension': [hypertension],
                               'heart_disease': [heart_disease],
                               'avg_glucose_level': [avg_glucose_level],
                               'bmi': [bmi],
                               'gender_Male': [gender_male],
                               'ever_married_Yes': [ever_married_yes],
                               'work_type_encoded': [work_type_encoded],
                               'Residence_type_encoded': [residence_encoded]})
    
    # Predicting stroke
    if st.sidebar.button('Predict'):
        prediction = predict_stroke(input_data)
        if prediction[0] == 1:
            st.sidebar.success('The patient is likely to have a stroke.')
        else:
            st.sidebar.success('The patient is unlikely to have a stroke.')

if __name__ == '__main__':
    main()
