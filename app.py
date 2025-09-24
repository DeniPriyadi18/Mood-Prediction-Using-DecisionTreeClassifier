import pandas as pd
import streamlit as st
import preprocessing


col1, col2= st.columns([1,5])
with col1:
    st.image("foto/images.jpg", width= 200)
with col2:
    st.header('Prediction Mood App (Prototype)')

df=  pd.DataFrame()

col1, col2, col3= st.columns(3)
with col1:
    sleep_duration= float(st.number_input(label="Sleep Duration(hrs)", value=1))
    df['Sleep Duration(hrs)'] = sleep_duration
with col2:
    meditation= int(st.number_input(label="Meditation(mins)", value= 10))
    df['Meditation(mins)']= meditation
with col3:
    exercise= int(st.number_input(label="Exercise(mins)", value=5))
    df['Exercise(mins)']= exercise

col1, col2=st.columns(2)
with col1:
    wakeup_time= st.time_input("Wake-Up Time")
    df['Wake-Up Time'] = wakeup_time
with col2:
    work_start_time= st.time_input("Work Start Time")
    df['Work Start Time']= work_start_time


col1, col2= st.columns(2)
with col1:
    breakfast= st.selectbox("Breakfast Type", options=['Skipped', 'Light', 'Protein-rich', 'Carb-rich', 'Heavy'])
    df['breakfast_type']= breakfast
with col2:
    journaling= st.selectbox("Journaling", options=['No', 'Yes'])
    df['journaling']= journaling

if st.button("Predict"):
    try:
        predicted_mood = preprocessing.predict_mood(wakeup_time, work_start_time, sleep_duration,
            meditation, exercise, breakfast, journaling)
        st.success(f"Today You will have a {predicted_mood} mood")
    
    except Exception as e:
        st.error(f"Error in Prediction: {str(e)}")

st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p>Developed by <strong>Deni Priyadi</strong> | © 2025</p>
    <p>📧 denipriyadi90@gmail.com | 
    <a href='https://github.com/DeniPriyadi18' target='_blank'>GitHub</a> | 
    <a href='https://www.linkedin.com/in/denipriyadi18/' target='_blank'>LinkedIn</a>
    </p>
    <p><em>Licensed under MIT License</em></p>
</div>
""", unsafe_allow_html=True)