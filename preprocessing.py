import pandas as pd
import numpy as np
import joblib

scaler= joblib.load('Model/scaler.joblib')
model= joblib.load('Model/predict_mood_by_morning_routine.pkl')

def time_to_minute(time_konv):
    if pd.isna(time_konv):
        return np.nan
    try:
        time_obj = pd.to_datetime(time_konv, format='%I:%M %p').time()
        return time_obj.hour * 60 + time_obj.minute
    except:
        return np.nan

def preprocess_time(wake_up_time, work_start_time):
    # Konversi waktu ke menit
    wake_up_minutes = time_to_minute(wake_up_time)
    work_start_minutes = time_to_minute(work_start_time)
    prep_time = work_start_minutes - wake_up_minutes
    return {
        'wake_up_minutes': wake_up_minutes,
        'prep_time': prep_time,
    }

def get_mappings():
    return {
        'breakfast_mapping': {
            'Skipped': 0,
            'Light': 1,
            'Protein-rich': 2,
            'Carb-rich': 3,
            'Heavy': 4
        },
        'journaling_mapping': {
            'No': 0,
            'Yes': 1
        }
    }

def preprocess_categorical(breakfast_type, journaling):
    mapping= get_mappings()

    breakfast_encoded= mapping['breakfast_mapping'][breakfast_type]
    journaling_encoded= mapping['journaling_mapping'][journaling]

    return breakfast_encoded, journaling_encoded

def preprocess(wake_up_time, work_start_time, sleep_duration, meditation, exercise, breakfast_type, journaling):
    time_features= preprocess_time(wake_up_time, work_start_time)
    breakfast_encoded, journaling_encoded= preprocess_categorical(breakfast_type, journaling)

    features_array= [
        time_features['wake_up_minutes'],
        sleep_duration,
        meditation,
        exercise,
        breakfast_encoded,
        journaling_encoded,
        time_features['prep_time']
    ]

    features_array= np.array(features_array).reshape(1, -1)

    features_scaled= scaler.transform(features_array)

    return features_scaled

def predict_mood(wake_up_time, work_start_time, sleep_duration, meditation, exercise, breakfast_type, journaling):
    preprocess_features= preprocess(wake_up_time, work_start_time, sleep_duration, meditation, exercise, breakfast_type, journaling)
    prediction= model.predict(preprocess_features)[0]
    mood_labels= {
        0 : 'Sad',
        2 : 'Happy'
    }

    predicted_mood= mood_labels[prediction]
    return predicted_mood