import pickle
from fastapi import APIRouter
import numpy as np
import pandas as pd
from app.alzihmers.models.alzimers_pre_data_input import DataInput, data
from fastapi.responses import JSONResponse

alzihmers_Router = APIRouter()
data = {
    "M/F": 0,
    "Age": 73,
    "EDUC": 8,
    "SES": 10.0,
    "MMSE": 25.0,
    "eTIV": 1151,
    "nWBV": 0.743,
    "ASF": 1.525
}

with open('app/alzihmers/trained_models/svm_alzihmers.pkl', 'rb') as f:
    svm = pickle.load(f)

with open('app/alzihmers/trained_models/AdaBoost_alzihmers.pkl', 'rb') as f:
    adaBoost = pickle.load(f) 

with open('app/alzihmers/trained_models/logistic_regresion_alzihmers1.pkl', 'rb') as f:
    logistic_regresion = pickle.load(f) 

with open('app/alzihmers/trained_models/Random_Forest_alzihmers.pkl', 'rb') as f:
    random_forest = pickle.load(f) 

with open('app/alzihmers/trained_models/Decision_tree_alzihmers.pkl', 'rb') as f:
    decision_tree = pickle.load(f) 

with open('app/alzihmers/scalers/alzihmers_scaler1.pkl','rb') as f: 
    scaler = pickle.load(f)

with open('app/alzihmers/trained_models/svm_alzihmers_withProba.pkl','rb') as f: 
    svm_proba = pickle.load(f)

# logistic_regression trained on scaled dataset with imputation (X_trainval_scaled )
@alzihmers_Router.get("/alzihmerLogisticRegresion")
async def predict():
    # numerical_data = np.array([data.dict().values()])  # Convert DataInput to a numerical array
    transformed_data = pd.DataFrame([data])
    scaled_data = scaler.transform(transformed_data)
    prediction = logistic_regresion.predict(scaled_data)
    prediction_list = prediction.tolist()
    return JSONResponse(content={"prediction": prediction_list})


# logistc Regresion with proba 
@alzihmers_Router.get("/alzihmerLogisticRegresionWithProba")
async def predict():
    # numerical_data = np.array([data.dict().values()])  # Convert DataInput to a numerical array
    transformed_data = pd.DataFrame([data])
    scaled_data = scaler.transform(transformed_data)
    try:
        proba = logistic_regresion.predict_proba(scaled_data)[0]
        prediction = int(proba[1] >= 0.5) # Use a threshold of 0.5 to convert the probabilities to binary predictions
    except Exception as e:
        return {'error': str(e)}

    # Convert the numpy float32 objects to Python floats
    proba_0 = float(proba[0])
    proba_1 = float(proba[1])

    # Return the predicted value and the probability estimates
    return {'prediction': prediction, 'probabillity of not having alzhimers disease': proba_0, 'probabillity of having alzhimers disease': proba_1}


# SVM  trained on scaled data (X_trainval_scaled) 
@alzihmers_Router.get("/alzihmerSVM")
async def predict():
    # numerical_data = np.array([data.dict().values()])  # Convert DataInput to a numerical array
    transformed_data = pd.DataFrame([data])
    scaled_data = scaler.transform(transformed_data)
    prediction = svm.predict(scaled_data)
    prediction_list = prediction.tolist()
    return JSONResponse(content={"prediction": prediction_list})


# SVM with proba 
@alzihmers_Router.get("/alzihmerSVMProba")
async def predict():
    # numerical_data = np.array([data.dict().values()])  # Convert DataInput to a numerical array
    transformed_data = pd.DataFrame([data])
    scaled_data = scaler.transform(transformed_data)
    try:
        proba = svm_proba.predict_proba(scaled_data)[0]
        prediction = int(proba[1] >= 0.5) # Use a threshold of 0.5 to convert the probabilities to binary predictions
    except Exception as e:
        return {'error': str(e)}

    # Convert the numpy float32 objects to Python floats
    proba_0 = float(proba[0])
    proba_1 = float(proba[1])

    # Return the predicted value and the probability estimates
    return {'prediction': prediction, 'probabillity of not having alzhimers disease': proba_0, 'probabillity of having alzhimers disease': proba_1}


# decision tree on scaled data (X_trainval_scaled)
@alzihmers_Router.get("/alzihmerDecision_Tree")
async def predict():
    # numerical_data = np.array([data.dict().values()])  # Convert DataInput to a numerical array
    transformed_data = pd.DataFrame([data])
    scaled_data = scaler.transform(transformed_data)
    prediction = decision_tree.predict(scaled_data)
    prediction_list = prediction.tolist()
    return JSONResponse(content={"prediction": prediction_list})

# decision tree with proba 
@alzihmers_Router.get("/alzihmerDecesionTreeWithProba")
async def predict():
    # numerical_data = np.array([data.dict().values()])  # Convert DataInput to a numerical array
    transformed_data = pd.DataFrame([data])
    scaled_data = scaler.transform(transformed_data)
    try:
        proba = decision_tree.predict_proba(scaled_data)[0]
        prediction = int(proba[1] >= 0.5) # Use a threshold of 0.5 to convert the probabilities to binary predictions
    except Exception as e:
        return {'error': str(e)}

    # Convert the numpy float32 objects to Python floats
    proba_0 = float(proba[0])
    proba_1 = float(proba[1])

    # Return the predicted value and the probability estimates
    return {'prediction': prediction, 'probabillity of not having alzhimers disease': proba_0, 'probabillity of having alzhimers disease': proba_1}



# random Forest on scaled data (X_trainval_scaled)
@alzihmers_Router.get("/alzihmerRandomForest")
async def predict():
    # numerical_data = np.array([data.dict().values()])  # Convert DataInput to a numerical array
    transformed_data = pd.DataFrame([data])
    scaled_data = scaler.transform(transformed_data)
    prediction = random_forest.predict(scaled_data)
    prediction_list = prediction.tolist()
    return JSONResponse(content={"prediction": prediction_list})


# adaBosst traned on scaled data (X_trainval_scaled)
@alzihmers_Router.get("/alzihmerAdaBoost")
async def predict():
    # numerical_data = np.array([data.dict().values()])  # Convert DataInput to a numerical array
    transformed_data = pd.DataFrame([data])
    scaled_data = scaler.transform(transformed_data)
    prediction = adaBoost.predict(scaled_data)
    prediction_list = prediction.tolist()
    return JSONResponse(content={"prediction": prediction_list})


# Ada Boost with proba 
@alzihmers_Router.get("/alzihmerAdaBoostWithProba")
async def predict():
    # numerical_data = np.array([data.dict().values()])  # Convert DataInput to a numerical array
    transformed_data = pd.DataFrame([data])
    scaled_data = scaler.transform(transformed_data)
    try:
        proba = adaBoost.predict_proba(scaled_data)[0]
        prediction = int(proba[1] >= 0.5) # Use a threshold of 0.5 to convert the probabilities to binary predictions
    except Exception as e:
        return {'error': str(e)}

    # Convert the numpy float32 objects to Python floats
    proba_0 = float(proba[0])
    proba_1 = float(proba[1])

    # Return the predicted value and the probability estimates
    return {'prediction': prediction, 'probabillity of not having alzhimers disease': proba_0, 'probabillity of having alzhimers disease': proba_1}
