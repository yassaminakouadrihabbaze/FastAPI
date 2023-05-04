import pickle

from fastapi import APIRouter, Request
import pandas as pd
from pydantic import BaseModel
from fastapi.responses import JSONResponse

kidney_desease_router = APIRouter()



# df['class'] = df['class'].map({'ckd': 0, 'not ckd': 1})
# df['class'] = pd.to_numeric(df['class'], errors='coerce')



with open('knn_kidney(1).pkl','rb') as f:
    knn_model = pickle.load(f)

with open('gradient_boosting_classifier_kidney(1).pkl','rb') as f:
    gbc_model = pickle.load(f)

class kidney_dis_pre_input(BaseModel):
    age: float
    blood_pressure: float
    specific_gravity: float
    albumin: float
    sugar: float
    red_blood_cells: int
    pus_cell: int
    pus_cell_clumps: int
    bacteria: int
    blood_glucose_random: float
    blood_urea: float
    serum_creatinine: float
    sodium: float
    potassium: float
    haemoglobin: float
    packed_cell_volume: float
    white_blood_cell_count: float
    red_blood_cell_count: float
    hypertension: int
    diabetes_mellitus: int
    coronary_artery_disease: int
    appetite: int
    peda_edema: int



input_data = { 'age':92,
    'blood_pressure':71.0,
    'specific_gravity':70.0,
    'albumin':1.010,
    'sugar':3.0,
    'red_blood_cells':2,
    'pus_cell':0,
    'pus_cell_clumps':1,
    'bacteria':1,
    'blood_glucose_random':219.0,
    'blood_urea':82.0,
    'serum_creatinine':3.6,
    'sodium':133.0,
    'potassium':4.4,
    'haemoglobin':10.4,
    'packed_cell_volume':33.0,
    'white_blood_cell_count':5600.0,
    'red_blood_cell_count':3.6,
    'hypertension':1,
    'diabetes_mellitus':1,
    'coronary_artery_disease':1,
    'appetite':0,
    'peda_edema':0
}


@kidney_desease_router.get("/kidney_desease/Knn")
async def predict_with_knn():
    data = pd.DataFrame([json_data])
    prediction = knn_model.predict(data)
    prediction_list = prediction.tolist()
    return JSONResponse(content={"prediction": prediction_list})

json_data = {
    "age": 92,
    "blood_pressure": 71.0,
    "specific_gravity": 70.0,
    "albumin": 1.010,
    "sugar": 3.0,
    "red_blood_cells": 1,
    "pus_cell": 0,
    "pus_cell_clumps": 1,
    "bacteria": 1,
    "blood_glucose_random": 219.0,
    "blood_urea": 82.0,
    "serum_creatinine": 3.6,
    "sodium": 133.0,
    "potassium": 4.4,
    "haemoglobin": 10.4,
    "packed_cell_volume": 33.0,
    "white_blood_cell_count": 5600.0,
    "red_blood_cell_count": 3.6,
    "hypertension": 1,
    "diabetes_mellitus": 1,
    "coronary_artery_disease": 1,
    "appetite": 0,
    "peda_edema": 0,
    "aanemia": 0
}

@kidney_desease_router.post("/kidney_desease/KnnWithProba")
async def predict_with_knnn(request: Request):
    try:
        print("heeeeeeeeeeeeeey")
        json_data = await request.json()
        print("Received JSON data:", json_data)
        try:
            data = pd.DataFrame([json_data])
            print("Data:", data)
            proba = knn_model.predict_proba(data)[0]
            prediction = int(proba[1] >= 0.5) # Use a threshold of 0.5 to convert the probabilities to binary predictions
        except Exception as e:
            print("the error is ",e)
            return {'error': str(e)}

        # Convert the numpy float32 objects to Python floats
        proba_0 = float(proba[0])
        proba_1 = float(proba[1])

        # Return the predicted value and the probability estimates
        return {'prediction': prediction, 'proba_0': proba_0, 'proba_1': proba_1}
    except Exception as e:
        return {'error': e}



# Gradient Boosting Classifier
@kidney_desease_router.get("/kidney_desease/GradientBoostingClassifier")
async def predict_with_gbc():
    data = pd.DataFrame([json_data])
    try:
        prediction = gbc_model.predict(data)
    except Exception as e:
        return {'error': str(e)}
    prediction_list = prediction.tolist()
    return JSONResponse(content={"prediction": prediction_list})


# Gradient Boosting Classifier with probability to use with client
@kidney_desease_router.post("/kidney_desease/GradientBoostingClassifierWithProba")
async def predict_with_gbc(resquest: Request):
    
    json_data = await  resquest.json()
    data = pd.DataFrame([json_data])
    print('dataaaaaaaaaaa',data)
    try:
        proba = gbc_model.predict_proba(data)[0]
        prediction = int(proba[1] >= 0.5) # Use a threshold of 0.5 to convert the probabilities to binary predictions
    except Exception as e:
        return {'error': str(e)}
    
    proba_0 = float(proba[0])
    proba_1 = float(proba[1])
    
    # convertion to dicimal 
    # 5.46259808357893e-05 is equivalent to 0.0000546259808357893 in decimal notation.
    # probability = 5.46259808357893e-05
    probability_decimal = '{:.10f}'.format(proba_1)


    # Return the predicted value and the probability estimates
    return {'prediction': prediction, 'proba_0': proba_0, 'proba_1': probability_decimal}


# Gradient Boosting Classifier with probability
@kidney_desease_router.get("/kidney_desease/GradientBoostingClassifierWithProba")
async def predict_with_gbc():
    data = pd.DataFrame([json_data])
    try:
        proba = gbc_model.predict_proba(data)[0]
        prediction = int(proba[1] >= 0.5) # Use a threshold of 0.5 to convert the probabilities to binary predictions
    except Exception as e:
        return {'error': str(e)}
    
    proba_0 = float(proba[0])
    proba_1 = float(proba[1])

    # convertion to dicimal 
    # 5.46259808357893e-05 is equivalent to 0.0000546259808357893 in decimal notation.
    # probability = 5.46259808357893e-05
    # probability_decimal = '{:.10f}'.format(probability)


    # Return the predicted value and the probability estimates
    return {'prediction': prediction, 'probabillity of not having heart disease': proba_0, 'probabillity of having heart disease': proba_1}
