import pickle
from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from sklearn.preprocessing import MinMaxScaler

# Define your FastAPI app
diabities_router = APIRouter()

with open('diabities_random_forest_model.pkl','rb') as f:
    model = pickle.load(f)

class predict_diabities_input_data(BaseModel):
    Age: float
    Gender: int
    Polyuria: int
    Polydipsia: int
    sudden_weight_loss: int
    weakness: int
    Polyphagia: int
    Genital_thrush: int
    visual_blurring: int
    Itching: int
    Irritability: int
    delayed_healing: int
    partial_paresis: int
    muscle_stiffness: int
    Alopecia: int
    Obesity: int

no_diabities_input_data = {0.405405, 	1, 	0, 	0, 	0, 	1, 	0, 	0, 	0, 	1, 	0, 	1, 	0, 	0, 	1, 	0}

yes_diabities_input_data ={'Age' :0.364865, 'Gender' :1, 'Polyuria' :1,'Polydipsia' :1, 'sudden weight loss' :1, 'weakness':	1, 	'Polyphagia' :0, 	'Genital thrush' :1, 'visual blurring' :	0, 
                           	'Itching' :0, 'Irritability' :	0, 'delayed healing' :	0, 'partial paresis' :	0,'muscle stiffness' : 	0,'Alopecia' : 	0,'Obesity' : 	0}
@diabities_router.post('/predict/diabities')
async def predict():
    # scaler = MinMaxScaler()
    # data[['Age']] = scaler.fit_transform(data[['Age']])
    data = pd.DataFrame([yes_diabities_input_data])
    prediction = model.predict(data)
    prediction_list = prediction.tolist()
    return JSONResponse(content={"prediction": prediction_list})
