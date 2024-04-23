import streamlit as st
import pickle
import numpy as np


def predict_stroke_risk(input_data):
    rf_model=pickle.dumps(open('saved_model.pkl','rb'))
    prediction = rf_model.predict(input_data)
    return prediction

# Define the Streamlit app
def main():
    st.title('Stroke Prediction App')

    # Collect user input
    age = st.number_input('Age', min_value=0, max_value=120, value=40)
    hypertension = st.selectbox('Hypertension', [0, 1])
    heart_disease = st.selectbox('Heart Disease', [0, 1])
    avg_glucose_level = st.number_input('Average Glucose Level', min_value=0, max_value=300, value=100)
    bmi = st.number_input('BMI', min_value=0, max_value=100, value=25)
    gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
    ever_married = st.selectbox('Ever Married', ['Yes', 'No'])
    work_type = st.selectbox('Work Type', ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
    Residence_type = st.selectbox('Residence Type', ['Urban', 'Rural'])
    smoking_status = st.selectbox('Smoking Status', ['formerly smoked', 'never smoked', 'smokes', 'Unknown'])

    # Convert categorical variables to dummy variables
    gender_male = 1 if gender == 'Male' else 0
    gender_female = 1 if gender == 'Female' else 0
    gender_other = 1 if gender == 'Other' else 0

    ever_married_yes = 1 if ever_married == 'Yes' else 0
    ever_married_no = 1 if ever_married == 'No' else 0

    # Make prediction
    input_data = pd.DataFrame({
        'age': [age],
        'hypertension': [hypertension],
        'heart_disease': [heart_disease],
        'avg_glucose_level': [avg_glucose_level],
        'bmi': [bmi],
        'gender_Male': [gender_male],
        'gender_Female': [gender_female],
        'gender_Other': [gender_other],
        'ever_married_Yes': [ever_married_yes],
        'ever_married_No': [ever_married_no],
        'work_type': [work_type],
        'Residence_type': [Residence_type],
        'smoking_status': [smoking_status]
    })

    prediction = predict_stroke_risk(input_data)

    st.write('### Prediction')
    if prediction == 1:
        st.write('The individual is at risk of stroke.')
    else:
        st.write('The individual is not at risk of stroke.')

if __name__ == '__main__':
    main()