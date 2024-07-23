# -*- coding: utf-8 -*-


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('df_diabete_test.csv', 'rb'))

heart_disease_model = pickle.load(open('df_coeur_test.csv','rb'))

liver_model = pickle.load(open('liver_test.csv', 'rb'))

kidney_model = pickle.load(open('kidney_test.csv', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'liver_model',
                           'kidney_model'],
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
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
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
        age = st.text_input('Age')
        
    with col2:
        total_bilirubin = st.text_input('Total_Bilirubin')
        
    with col3:
        alkaline_phosphotase = st.text_input('Alkaline_Phosphotase')
        
    with col4:
        alamine_aminotransferase = st.text_input('Alamine_Aminotransferase')
        
    with col5:
        albumin_and_globulin_ratio = st.text_input('Albumin_and_Globulin_Ratio')
        
    with col1:
        gender_female = st.text_input('Gender_Female')
        
    with col2:
        gender_male = st.text_input('Gender_Male')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP_Shimmer')
        
         
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

# Breast Cancer Prediction Page
if (selected == "Breast Cancer Prediction"):
    
    # page title
    st.title("Breast Cancer Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  

    with col1:
        fo = st.number_input('mean radius')
        
    with col2:
        fhi = st.number_input('mean texture')
        
    with col3:
        flo = st.number_input('mean perimeter')
        
    with col4:
        Jitter_percent = st.number_input('mean area')
        
    with col5:
        Jitter_Abs = st.number_input('mean smoothness')
        
    with col1:
        RAP = st.number_input('mean compactness')
        
    with col2:
        PPQ = st.number_input('mean concavity')
        
    with col3:
        DDP = st.number_input('mean concave points')
        
    with col4:
        Shimmer = st.number_input('mean symmetry')
        
    with col5:
        Shimmer_dB = st.number_input('mean fractal dimension')
        
    with col1:
        APQ3 = st.number_input('radius error')
        
    with col2:
        APQ4 = st.number_input('texture error')

    with col3:
        APQ5 = st.number_input('perimeter error')
        
    with col4:
        APQ = st.number_input('area error')
        
    with col5:
        DDA = st.number_input('smoothness error')
        
    with col1:
        NHR = st.number_input('compactness error')
        
    with col2:
        HNR = st.number_input('concavity error')
        
    with col3:
        RPDE = st.number_input('concave points error')
        
    with col4:
        DFA = st.number_input('symmetry error')

    with col5:
        spread1 = st.number_input('fractal dimension error')
        
    with col1:
        spread2 = st.number_input('worst radius')
        
    with col2:
        D2 = st.number_input('worst texture')
        
    with col3:
        PPE = st.number_input('worst perimeter')

        
    with col4:
        wa = st.number_input('worst area')
        
    with col5:
        ws = st.number_input('worst smoothness')
        
    with col1:
        w_cm = st.number_input('worst compactness')

    with col2:
        w_con = st.number_input('worst concavity')
        
    with col3:
        w_cp = st.number_input('worst concave points')

        
    with col4:
        w_sym = st.number_input('worst symmetry')
        
    with col5:
        w_fd = st.number_input('worst fractal dimension')
        
    
    
    # code for Prediction
    cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        cancer_prediction = BreastCancer_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ4,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE, wa, ws, w_cm, w_con, w_cp, w_sym, w_fd]])                          
        
        if (cancer_prediction[0] == 1):
          cancer_diagnosis = "The Breast Cancer is Benign"
        else:
          cancer_diagnosis = "The Breast cancer is Malignant"
        
    st.warning(cancer_diagnosis)

