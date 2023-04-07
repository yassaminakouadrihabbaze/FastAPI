import json
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
#import joblib
import pandas as pd
import pickle 
import xgboost as xgb
# define the FastAPI app
from sklearn.preprocessing import MinMaxScaler


cardio2 = APIRouter()

# load the trained model
# model = joblib.load("heart_disease_xgboost.pkl")

with open('cardio_xgbox.pkl', 'rb') as f:
    model = pickle.load(f)

# define the input schema using Pydantic
class InputFeatures(BaseModel):
    age: float
    resting_blood_pressure: float
    cholesterol: float
    fasting_blood_sugar: int
    max_heart_rate_achieved: float
    exercise_induced_angina: int
    st_depression: float
    sex_male: int
    chest_pain_type_atypical_angina: int
    chest_pain_type_non_anginal_pain: int
    chest_pain_type_typical_angina: int
    rest_ecg_left_ventricular_hypertrophy: int
    rest_ecg_normal: int
    st_slope_flat: int
    st_slope_upsloping: int

# define the prediction route
input_data = [0.693878, 0.301075, 0.572301, 0, 0.266667, 0, 0.376623, 1, 1, 0, 0, 1, 0, 1, 0]
data = {'age': 0.693878, 'resting_blood_pressure': 0.301075, 'cholesterol': 0.572301, 'fasting_blood_sugar': 0, 'max_heart_rate_achieved': 0.266667, 'exercise_induced_angina': 0, 'st_depression': 0.376623, 'sex_male': 1, 'chest_pain_type_atypical angina': 1, 'chest_pain_type_non-anginal pain': 0, 'chest_pain_type_typical angina': 0, 'rest_ecg_left ventricular hypertrophy': 1, 'rest_ecg_normal': 0, 'st_slope_flat': 1, 'st_slope_upsloping': 0}
@cardio2.post("/predict2")
async def predict():
    # Convert the input dictionary to a pandas DataFrame
    input_df = pd.DataFrame([data])

    # Use the XGBoost model to make predictions
    try:
        prediction = model.predict(input_df)[0]
    except Exception as e:
        return {'error': str(e)}

    prediction = prediction.item()
    # Return the predicted value
    return {'prediction': prediction}
data = {'age': 0.693878, 'resting_blood_pressure': 0.301075, 'cholesterol': 0.572301, 'fasting_blood_sugar': 0, 
        'max_heart_rate_achieved': 0.266667, 'exercise_induced_angina': 0, 'st_depression': 0.376623, 'sex_male': 1,
          'chest_pain_type_atypical angina': 1, 'chest_pain_type_atypical angina': 0, 'chest_pain_type_typical angina': 0, 
          'rest_ecg_left ventricular hypertrophy': 1, 'rest_ecg_normal': 0, 'st_slope_flat': 1, 'st_slope_upsloping': 0}

yes_desease_data = {'age': 45, 'resting_blood_pressure':	110, 'cholesterol': 264, 	'fasting_blood_sugar': 0, 	
                   'max_heart_rate_achieved':132,  'exercise_induced_angina':	0 ,'st_depression':	1.2 ,	'sex_male': 1 ,
                       	'chest_pain_type_atypical angina':1, 	'chest_pain_type_non-anginal pain': 0 ,'chest_pain_type_typical angina': 0,
                        'rest_ecg_left ventricular hypertrophy': 	1,  'rest_ecg_normal':	0 , 'st_slope_flat': 1, 'st_slope_upsloping': 1 }

no_desease_data = {'age': 54, 'resting_blood_pressure':	150, 'cholesterol': 195, 	'fasting_blood_sugar': 0, 	
                   'max_heart_rate_achieved':122,  'exercise_induced_angina':	0 ,'st_depression':	0.0 ,	'sex_male': 1,
                       	'chest_pain_type_atypical angina':0, 	'chest_pain_type_non-anginal pain': 1 ,'chest_pain_type_typical angina': 0,
                        'rest_ecg_left ventricular hypertrophy': 	0,  'rest_ecg_normal':	1 , 'st_slope_flat': 0, 'st_slope_upsloping': 1 }


@cardio2.post("/predict_with_proba")
async def predict_with_proba():
    # Convert the input dictionary to a pandas DataFrame
    input_df = pd.DataFrame([no_desease_data])
    scaler = MinMaxScaler()
     # Scale the numerical features
    numerical_cols = ['age', 'resting_blood_pressure', 'cholesterol', 'max_heart_rate_achieved', 'st_depression']
    # Fit the scaler object with the input data
    # scaler.fit(input_df[numerical_cols])
    input_df[numerical_cols] = scaler.fit_transform(input_df[numerical_cols])

    # Use the XGBoost model to make predictions
    try:
        proba = model.predict_proba(input_df)[0]
        prediction = int(proba[1] >= 0.5) # Use a threshold of 0.5 to convert the probabilities to binary predictions
    except Exception as e:
        return {'error': str(e)}

    # Convert the numpy float32 objects to Python floats
    proba_0 = float(proba[0])
    proba_1 = float(proba[1])

    # Return the predicted value and the probability estimates
    return {'prediction': prediction, 'probabillity of not having heart disease': proba_0, 'probabillity of having heart disease': proba_1}

async def predict(input_data: InputFeatures):
    input_df = pd.DataFrame([dict(input_data)])
    prediction = model.predict(input_df)[0]
    return {"prediction": prediction}


