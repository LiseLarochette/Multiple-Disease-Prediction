# -*- coding: utf-8 -*-
import pandas as pd
import pickle
import streamlit as st
from projet3_kidney import prediction_kidney
from projet_3_diabetes import prediction_diabete
from projet_3_liver import prediction_liver
from projet_3_coeur_py import prediction_maladie_cardiaque
from projet_3_breast_cancer import prediction_breastcancer
from streamlit_option_menu import option_menu


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Liver Prediction',
                           'Kidney Prediction','Breast Cancer Prediction'],
                          icons=['activity','heart-pulse','person', 'clipboard2-pulse'],
                          default_index=0)
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    # page title
    st.title('Diabetes Prediction using ML')
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        Insulin = st.text_input('Insulin Level')
    with col2:
        BMI = st.text_input('BMI value')
    with col3:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col1:
        Age = st.text_input('Age of the Person')
    # code for Prediction
    diab_diagnosis = ''
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex(1 for male, 0 for female)')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    # code for Prediction
    heart_diagnosis = ''
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
    st.success(heart_diagnosis)
# liver_model's Prediction Page
if (selected == "Liver Prediction"):
    # page title
    st.title("Liver's Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        Age = st.text_input('Age')
    with col2:
        Total_Bilirubin = st.text_input('Total_Bilirubin')
    with col3:
        Alkaline_Phosphotase = st.text_input('Alkaline_Phosphotase')
    with col4:
        Alamine_Aminotransferase = st.text_input('Alamine_Aminotransferase')
    with col5:
        Albumin_and_Globulin_Ratio = st.text_input('Albumin_and_Globulin_Ratio')
    with col1:
        Gender_Female = st.text_input('Gender_Female')
    with col2:
        Gender_Male = st.text_input('Gender_Male')
    # code for Prediction
    liver_diagnosis = ''
    # creating a button for Prediction
    if st.button("Liver's Test Result"):
        liver_prediction = liver_model.predict([[Age, Total_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Albumin_and_Globulin_Ratio, Gender_Female, Gender_Male]])
        if (liver_prediction[0] == 1):
          liver_diagnosis = "The person has Liver's disease"
        else:
          liver_diagnosis = "The person does not have Liver's disease"
    st.success(liver_diagnosis)
# Breast Cancer Prediction Page
if (selected == "Breast Cancer Prediction"):
    # page title
    st.title("Breast Cancer Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        radius_mean = st.number_input('mean radius')
    with col2:
        texture_mean = st.number_input('mean texture')
    with col3:
        perimeter_mean = st.number_input('mean perimeter')
    with col4:
        area_mean = st.number_input('mean area')
    with col5:
        smoothness_mean = st.number_input('mean smoothness')
    with col1:
        compactness_mean = st.number_input('mean compactness')
    with col2:
        concavity_mean = st.number_input('mean concavity')
    with col3:
        points_mean = st.number_input('mean concave points')
    with col4:
        symmetry_mean = st.number_input('mean symmetry')
    with col5:
        fractal_dimension_mean = st.number_input('mean fractal dimension')
    with col1:
        radius_se = st.number_input('radius error')
    with col2:
        texture_se = st.number_input('texture error')
    with col3:
        perimeter_se = st.number_input('perimeter error')
    with col4:
        area_se = st.number_input('area error')
    with col5:
        smoothness_se = st.number_input('smoothness error')
    with col1:
        compactness_se = st.number_input('compactness error')
    with col2:
        concavity_se = st.number_input('concavity error')
    with col3:
        points_se = st.number_input('concave points error')
    with col4:
        symmetry_se = st.number_input('symmetry error')
    with col5:
        fractal_dimension_se = st.number_input('fractal dimension error')
    with col1:
        radius_worst = st.number_input('worst radius')
    with col2:
        texture_worst = st.number_input('worst texture')
    with col3:
        perimeter_worst = st.number_input('worst perimeter')
    with col4:
        area_worst = st.number_input('worst area')
    with col5:
        smoothness_worst = st.number_input('worst smoothness')
    with col1:
        compactness_worst = st.number_input('worst compactness')
    with col2:
        concavity_worst = st.number_input('worst concavity')
    with col3:
        points_worst = st.number_input('worst concave points')
    with col4:
        symmetry_worst = st.number_input('worst symmetry')
    with col5:
        fractal_dimension_worst = st.number_input('worst fractal dimension')
    # code for Prediction
    cancer_diagnosis = ''
    # creating a button for Prediction
    if st.button("Breast Cancer Test Result"):
        cancer_prediction = BreastCancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean,
 points_mean, symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,points_worst,symmetry_worst,fractal_dimension_worst]])
        if (cancer_prediction[0] == 1):
          cancer_diagnosis = "The Breast Cancer is Benign"
        else:
          cancer_diagnosis = "The Breast cancer is Malignant"
    st.warning(cancer_diagnosis)
