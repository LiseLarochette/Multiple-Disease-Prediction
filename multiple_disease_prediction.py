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
                          icons=['activity','heart-pulse','person','','clipboard2-pulse'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    # page title
    st.title('Diabetes Prediction using ML')
    diabete_uploaded_file = st.file_uploader("Choose a file",type="csv")
    
    # getting the input data from the user
    Pregnancies = None
    Glucose = None
    BloodPressure = None
    Insulin = None
    BMI = None
    DiabetesPedigreeFunction = None
    Age = None
    if diabete_uploaded_file is not None:
        df_test = pd.read_csv(diabete_uploaded_file)
        Pregnancies = df_test["Pregnancies"][0]
        Glucose = df_test["Glucose"][0]
        BloodPressure = df_test["Blood_pressure"][0]
        Insulin = df_test['Insulin'][0]
        BMI = df_test['BMI'][0]
        DiabetesPedigreeFunction = df_test['DiabetesPedigreeFunction'][0]
        Age = df_test['Age'][0]
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', value = Pregnancies)
    with col2:
        Glucose = st.text_input('Glucose Level', value = Glucose)
    with col3:
        BloodPressure = st.text_input('Blood Pressure value', value = BloodPressure)
    with col1:
        Insulin = st.text_input('Insulin Level', value = Insulin)
    with col2:
        BMI = st.text_input('BMI value', value = BMI)
    with col3:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', value = DiabetesPedigreeFunction)
    with col1:
        Age = st.text_input('Age of the Person', value = Age)
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_diagnosis = prediction_diabete([[Pregnancies, Glucose, BloodPressure, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction using ML')
    heart_uploaded_file = st.file_uploader("Choose a file",type="csv")
    age = None
    sex = None
    cp = None
    trestbps = None
    chol = None
    fbs = None
    restecg = None
    thalach = None
    exang = None
    oldpeak = None
    slope = None
    ca = None
    thal = None
    if heart_uploaded_file is not None:
        df_test = pd.read_csv(heart_uploaded_file)
        age = df_test["age"][0]
        sex = df_test["sex"][0]
        cp = df_test["cp"][0]
        trestbps = df_test['trestbps'][0]
        chol = df_test['chol'][0]
        fbs = df_test['fbs'][0]
        restecg = df_test['restecg'][0]
        thalach = df_test['thalach'][0]
        exang = df_test['exang'][0]
        oldpeak = df_test['oldpeak'][0]
        slope = df_test['slope'][0]
        ca = df_test['ca'][0]
        thal = df_test['thal'][0]
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age',value=age)
    with col2:
        sex = st.text_input('Sex(1 for male, 0 for female)',value=sex)
    with col3:
        cp = st.text_input('Chest Pain types', value = cp)
    with col1:
        trestbps = st.text_input('Resting Blood Pressure', value = trestbps)
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', value = chol)
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', value = fbs)
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', value = restecg)
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', value = thalach)
    with col3:
        exang = st.text_input('Exercise Induced Angina', value = exang)
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', value = oldpeak)
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', value = slope)
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy', value = ca)
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', value = thal)
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):                        
        heart_diagnosis = prediction_maladie_cardiaque([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        
    st.success(heart_diagnosis)



# kidney_model's Prediction Page
if (selected == "Kidney Prediction"):

    
    # page title
    st.title("kidney's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5) 
    
    with col1:
        age = st.text_input('Age')
    with col2:
        bp = st.text_input('Blood Pressure (mmHg)')
    with col3:
        sg = st.text_input('Specific Gravity')
    with col4:
        al = st.text_input('Albumin')
    with col5:
        su = st.text_input('Sugar')
    with col1:
        rbc = st.text_input('Red Blood Cells (normal or anormal)')
    with col2:
        pc = st.text_input('Pus Cell (present or notpresent)')
    with col3:
        pcc = st.text_input('Pus Cell Clumps (present or notpresent)')
    with col4:
        ba = st.text_input('Bacteria')
    with col5:
        bgr = st.text_input('Blood Glucose Random')
    with col1:
        bu = st.text_input('Blood Urea')
    with col2:
        sc = st.text_input('Serum Creatinine')
    with col3:
        sod = st.text_input('Sodium')
    with col4:
        pot = st.text_input('Potassium')
    with col5:
        hemo = st.text_input('Haemoglobin')
    with col1:
        pcv = st.text_input('Packed Cell Volume')
    with col2:
        wc = st.text_input('White Blood Cell Count')
    with col3:
        rc = st.text_input('Red Blood Cell Count')
    with col4:
        htn = st.text_input('Hypertension (yes or no)')
    with col5:
        dm = st.text_input('Diabetes Mellitus (yes or no)')
    with col1:
        cad = st.text_input('Coronary Artery Disease (yes or no)')
    with col2:
        appet = st.text_input('Appetite (good or poor)')
    with col3:
        pe = st.text_input('Pedal Edema (yes or no)')
    with col4:
        ane = st.text_input('Anemia')       
    


    # code for Prediction
    kidney_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("kidney's Test Result"):
        kidney_prediction = kidney_model.predict([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, 
sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]])                          
        if (kidney_prediction[0] == 1):
          kidney_diagnosis = "The person has kidney's disease"
        else:
          kidney_diagnosis = "The person does not have kidney's disease"
        
    st.success(kidney_diagnosis)
        
    
 
    

# liver_model's Prediction Page
if (selected == "Liver Prediction"):
    # page title
    st.title("Liver's Disease Prediction using ML")
    liver_uploaded_file = st.file_uploader("Choose a file",type="csv")
    Age = None
    Total_Bilirubin = None
    Alkaline_Phosphotase = None
    Alamine_Aminotransferase = None
    Albumin_and_Globulin_Ratio = None
    Gender = None
    if liver_uploaded_file is not None:
        df_test = pd.read_csv(liver_uploaded_file)
        Age = df_test["Age"][0]
        Total_Bilirubin = df_test["Total_Bilirubin"][0]
        Alkaline_Phosphotase = df_test["Alkaline_Phosphotase"][0]
        Alamine_Aminotransferase = df_test["Alamine_Aminotransferase"][0]
        Albumin_and_Globulin_Ratio = df_test["Albumin_and_Globulin_Ratio"][0]
        Gender = df_test["Gender"][0]
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age of the Person', value = Age)
    with col2:
        Total_Bilirubin = st.text_input('Total Bilirubin', value = Total_Bilirubin)
    with col3:
        Alkaline_Phosphotase = st.text_input('Alkaline Phosphotase', value = Alkaline_Phosphotase)
    with col1:
        Alamine_Aminotransferase = st.text_input('Alamine Aminotransferase', value = Alamine_Aminotransferase)
    with col2:
        Albumin_and_Globulin_Ratio = st.text_input('Albumin and Globulin Ratio', value = Albumin_and_Globulin_Ratio)
    with col3:
        Gender = st.text_input('Gender', value = Gender)
        
         
        
        
    
    
    # code for Prediction
    liver_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Liver's Test Result"):
        liver_diagnosis = prediction_liver([[Age, Total_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Albumin_and_Globulin_Ratio, Gender]])                          
        
    st.success(liver_diagnosis)

# Breast Cancer Prediction Page
if (selected == "Breast Cancer Prediction"):
    # page title
    st.title("Breast Cancer Prediction using ML")
    breast_uploaded_file = st.file_uploader("Choose a file",type="csv")
    radius_mean = None
    texture_mean = None
    perimeter_mean = None
    area_mean = None
    smoothness_mean = None
    compactness_mean = None
    concavity_mean = None
    points_mean = None
    symmetry_mean = None
    fractal_dimension_mean = None
    radius_se = None
    texture_se = None
    perimeter_se = None
    area_se = None
    smoothness_se = None
    compactness_se = None
    concavity_se = None
    points_se = None
    symmetry_se = None
    fractal_dimension_se = None
    radius_worst = None
    texture_worst = None
    perimeter_worst = None
    area_worst = None
    smoothness_worst = None
    compactness_worst = None
    concavity_worst = None
    points_worst = None
    symmetry_worst = None
    fractal_dimension_worst = None
    if breast_uploaded_file is not None:
        df_test = pd.read_csv(breast_uploaded_file)
        radius_mean = df_test["radius_mean"][0]
        texture_mean = df_test["texture_mean"][0]
        perimeter_mean = df_test["perimeter_mean"][0]
        area_mean = df_test['area_mean'][0]
        smoothness_mean = df_test['smoothness_mean'][0]
        compactness_mean = df_test['compactness_mean'][0]
        concavity_mean = df_test['concavity_mean'][0]
        points_mean = df_test['concave points_mean'][0]
        symmetry_mean = df_test['symmetry_mean'][0]
        fractal_dimension_mean = df_test['fractal_dimension_mean'][0]
        radius_se = df_test['radius_se'][0]
        texture_se = df_test['texture_se'][0]
        perimeter_se = df_test['perimeter_se'][0]
        area_se = df_test["area_se"][0]
        smoothness_se = df_test["smoothness_se"][0]
        compactness_se = df_test["compactness_se"][0]
        concavity_se = df_test['concavity_se'][0]
        points_se = df_test['concave points_se'][0]
        symmetry_se = df_test['symmetry_se'][0]
        fractal_dimension_se = df_test['fractal_dimension_se'][0]
        radius_worst = df_test['radius_worst'][0]
        texture_worst =df_test['texture_worst'][0]
        perimeter_worst = df_test['perimeter_worst'][0]
        area_worst = df_test['area_worst'][0]
        smoothness_worst = df_test['smoothness_worst'][0]
        compactness_worst = df_test['compactness_worst'][0]
        concavity_worst = df_test['concavity_worst'][0]
        points_worst = df_test['concave points_worst'][0]
        symmetry_worst = df_test['symmetry_worst'][0]
        fractal_dimension_worst = df_test['fractal_dimension_worst'][0]
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        radius_mean = st.number_input('mean radius', value = radius_mean)
    with col2:
        texture_mean = st.number_input('mean texture', value = texture_mean)
    with col3:
        perimeter_mean = st.number_input('mean perimeter', value = perimeter_mean)
    with col4:
        area_mean = st.number_input('mean area', value = area_mean)
    with col5:
        smoothness_mean = st.number_input('mean smoothness', value = smoothness_mean  )
    with col1:
        compactness_mean = st.number_input('mean compactness', value = compactness_mean)
    with col2:
        concavity_mean = st.number_input('mean concavity', value = concavity_mean)
    with col3:
        points_mean = st.number_input('mean concave points', value =  points_mean )
    with col4:
        symmetry_mean = st.number_input('mean symmetry', value = symmetry_mean)
    with col5:
        fractal_dimension_mean = st.number_input('mean fractal dimension', value = fractal_dimension_mean)
    with col1:
        radius_se = st.number_input('radiuserror', value = radius_se)
    with col2:
        texture_se = st.number_input('texture error', value = texture_se )
    with col3:
        perimeter_se = st.number_input('perimeter error', value = perimeter_se )
    with col4:
        area_se = st.number_input('area error', value = area_se )
    with col5:
        smoothness_se = st.number_input('smoothness error', value = smoothness_se )
    with col1:
        compactness_se = st.number_input('compactness error', value = compactness_se )
    with col2:
        concavity_se = st.number_input('concavity error', value =  concavity_se )
    with col3:
        points_se = st.number_input('concave points error', value = points_se)
    with col4:
        symmetry_se = st.number_input('symmetry error', value = symmetry_se)
    with col5:
        fractal_dimension_se = st.number_input('fractal dimension error', value = fractal_dimension_se)
    with col1:
        radius_worst = st.number_input('worst radius', value = radius_worst)
    with col2:
        texture_worst = st.number_input('worst texture', value = texture_worst )
    with col3:
        perimeter_worst = st.number_input('worst perimeter', value =  perimeter_worst)
    with col4:
        area_worst = st.number_input('worst area', value = area_worst)
    with col5:
        smoothness_worst = st.number_input('worst smoothness', value = smoothness_worst  )
    with col1:
        compactness_worst = st.number_input('worst compactness', value = compactness_worst)
    with col2:
        concavity_worst = st.number_input('worst concavity', value = concavity_worst)
    with col3:
        points_worst = st.number_input('worst concave points', value =  points_worst )
    with col4:
        symmetry_worst = st.number_input('worst symmetry', value = symmetry_worst )
    with col5:
        fractal_dimension_worst = st.number_input('worst fractal dimension', value =  fractal_dimension_worst )
    
    # code for Prediction
    cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        cancer_prediction = prediction_breastcancer([[radius_mean,
            texture_mean,
            perimeter_mean,
            area_mean,
            smoothness_mean,
            compactness_mean,
            concavity_mean,
            points_mean,
            symmetry_mean,
            fractal_dimension_mean,
            radius_se,
            texture_se,
            perimeter_se,
            area_se,
            smoothness_se,
            compactness_se,
            concavity_se,
            points_se,
            symmetry_se,
            fractal_dimension_se,
            radius_worst,
            texture_worst,
            perimeter_worst,
            area_worst,
            smoothness_worst,
            compactness_worst,
            concavity_worst,
            points_worst,
            symmetry_worst,
            fractal_dimension_worst]])
        
    st.warning(cancer_diagnosis)
