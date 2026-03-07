import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="ArogyaM",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('ArogyaM - Smart Predictions for Better Health',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Patient_id = st.text_input('Patient ID')
    
    with col2:
        Patient_name = st.text_input('Patient Name')
            
    with col3:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col1:
        Glucose = st.text_input('Glucose Level')

    with col2:
        BloodPressure = st.text_input('Blood Pressure value')

    with col3:
        SkinThickness = st.text_input('Skin Thickness value')

    with col1:
        Insulin = st.text_input('Insulin Level')

    with col2:
        BMI = st.text_input('BMI value')

    with col3:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col1:
        Age = st.text_input('Patient Age')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        Patient_id = st.text_input('Patient ID')
    
    with col2:
        Patient_name = st.text_input('Patient Name')

    with col3:
        age = st.text_input('Patient Age')

    with col1:
        sex = st.text_input('Sex')

    with col2:
        cp = st.text_input('Chest Pain types')

    with col3:
        trestbps = st.text_input('Resting Blood Pressure')

    with col1:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col2:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col3:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col1:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col2:
        exang = st.text_input('Exercise Induced Angina')

    with col3:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col1:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col2:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col3:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        
        st.success(heart_diagnosis)
        
        # Generate report content
        report_content = f"""
        HEART DISEASE PREDICTION REPORT
        
        Patient ID: {Patient_id}
        Patient Name: {Patient_name}
        Age: {age}
        Sex: {sex}
        Chest Pain Types: {cp}
        Resting Blood Pressure: {trestbps}
        Serum Cholesterol: {chol} mg/dl
        Fasting Blood Sugar > 120 mg/dl: {fbs}
        Resting ECG Results: {restecg}
        Maximum Heart Rate: {thalach}
        Exercise Induced Angina: {exang}
        ST Depression: {oldpeak}
        Slope of Peak Exercise ST: {slope}
        Major Vessels Colored: {ca}
        Thalassemia: {thal}
        
        DIAGNOSIS: {heart_diagnosis}
        
        Report Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        st.download_button(
            label="📄 Download Patient Report",
            data=report_content,
            file_name=f"heart_disease_report_{Patient_id}.txt",
            mime="text/plain"
        )

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        Patient_id = st.text_input('Patient ID')
    
    with col2:
        Patient_name = st.text_input('Patient Name')

    with col3:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col4:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col5:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col3:
        RAP = st.text_input('MDVP:RAP')

    with col4:
        PPQ = st.text_input('MDVP:PPQ')

    with col5:
        DDP = st.text_input('Jitter:DDP')

    with col1:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col2:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col3:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col4:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col5:
        APQ = st.text_input('MDVP:APQ')

    with col1:
        DDA = st.text_input('Shimmer:DDA')

    with col2:
        NHR = st.text_input('NHR')

    with col3:
        HNR = st.text_input('HNR')

    with col4:
        RPDE = st.text_input('RPDE')

    with col5:
        DFA = st.text_input('DFA')

    with col1:
        spread1 = st.text_input('spread1')

    with col2:
        spread2 = st.text_input('spread2')

    with col3:
        D2 = st.text_input('D2')

    with col4:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
        st.success(parkinsons_diagnosis)
        
        # Generate report content
        report_content = f"""
        PARKINSON'S DISEASE PREDICTION REPORT
        
        Patient ID: {Patient_id}
        Patient Name: {Patient_name}
        MDVP:Fo(Hz): {fo}
        MDVP:Fhi(Hz): {fhi}
        MDVP:Flo(Hz): {flo}
        MDVP:Jitter(%): {Jitter_percent}
        MDVP:Jitter(Abs): {Jitter_Abs}
        MDVP:RAP: {RAP}
        MDVP:PPQ: {PPQ}
        Jitter:DDP: {DDP}
        MDVP:Shimmer: {Shimmer}
        MDVP:Shimmer(dB): {Shimmer_dB}
        Shimmer:APQ3: {APQ3}
        Shimmer:APQ5: {APQ5}
        MDVP:APQ: {APQ}
        Shimmer:DDA: {DDA}
        NHR: {NHR}
        HNR: {HNR}
        RPDE: {RPDE}
        DFA: {DFA}
        spread1: {spread1}
        spread2: {spread2}
        D2: {D2}
        PPE: {PPE}
        
        DIAGNOSIS: {parkinsons_diagnosis}
        
        Report Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        st.download_button(
            label="📄 Download Patient Report",
            data=report_content,
            file_name=f"parkinsons_report_{Patient_id}.txt",
            mime="text/plain"
        )
