import time

import streamlit as st
import sklearn
import pickle
import numpy as np
from numpy import dtype
from altair.theme import options


model = pickle.load(open('/Users/arun/Downloads/Arun.pkl','rb'))

def db_pred(gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level):
    ip=np.array([[(gender),int(age),(hypertension),(heart_disease),(smoking_history),float(bmi),
                  float(HbA1c_level),int(blood_glucose_level)]],dtype=np.float64)
    result = model.predict(ip)
    return result

def main():
    st.title("Dr M.B.B.S. 👨🏻‍⚕ Diabetics Prediction ML️ 🏥")

    gender = st.selectbox("Gender",options=["Male","Female","Other"])
    gender_map = {'Male':1, 'Female': 0, 'Other':2}
    gender_value = gender_map[gender]

    age = st.text_input("Age:")

    hypertension = st.selectbox("Hypertension",options = ['Yes', 'No'])
    hypertension_map = {'Yes':1, 'No':0}
    hypertension_value = hypertension_map[hypertension]

    heart_disease = st.selectbox("Heart Disease",options=['Yes', 'No'])
    heart_disease_map = {'Yes':1, 'No':0}
    heart_disease_value = heart_disease_map[heart_disease]

    smoking_history = st.selectbox("Smoking History", options = ['Decline to provide info','Current','Ever','Former','Never','Not Current'])
    smoking_history_map = {'Decline to provide info':0,'Current':1,'Ever':2,'Former':3,'Never':4,'Not Current':5}
    smoking_history_values = smoking_history_map[smoking_history]
    bmi = st.text_input("BMI")
    HbA1c_level = st.text_input("HbA1c Level")
    blood_glucose_level = st.text_input("Blood Glucose")

    result_placeholder = st.empty()
    result_placeholder1 = st.empty()
    gif_holder = st.empty()

    if st.button("Predict"):
        try:
            gif = "/Users/arun/Downloads/Vasool_Raja_MBBS_4.gif"
            gif_holder.image(gif,caption = 'Processing', use_container_width=True)
            time.sleep(5)
            gif_holder.empty()

            op = db_pred(gender_value,age, hypertension_value, heart_disease_value,
                         smoking_history_values, bmi, HbA1c_level, blood_glucose_level)

            if op == 1:
                result_placeholder.markdown("""<div style ="text-align: center;font-size: 60 px; color: red;">
                                You are diabetic 😢
                                </div>""", unsafe_allow_html=True)
                result_placeholder1.audio("/Users/arun/Downloads/Avlothan Nammala Mudichu Vittinga Ponga Dialogue-[AudioTrimmer.com].mp3",autoplay=True)
            else:
                result_placeholder.markdown("""<div style ="text-align: center;font-size: 60 px; color: green;">
                You are not diabetic 🎉
                </div>""", unsafe_allow_html=True)
                st.balloons()
        except ValueError as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()



