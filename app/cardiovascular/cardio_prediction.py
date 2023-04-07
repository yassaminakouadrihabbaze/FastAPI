import pickle
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

# Define your FastAPI app
cardio_router = APIRouter()

# Define the input data schema using Pydantic BaseModel
class CardioRequest(BaseModel):
    age: float
    gender: float
    height: float
    weight: float
    ap_hi: float
    ap_lo: float
    cholesterol: float
    gluc: float
    smoke: float
    alco: float
    active: float

# Load the saved model
with open('cardio_tree_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the route for making predictions
@cardio_router.post("/predict")
async def predict_cardio(cardio_request: CardioRequest):
    X = [[cardio_request.age, cardio_request.gender, cardio_request.height, cardio_request.weight,
          cardio_request.ap_hi, cardio_request.ap_lo, cardio_request.cholesterol, cardio_request.gluc,
          cardio_request.smoke, cardio_request.alco, cardio_request.active]]
         # prediction = model.predict_proba(X)[:, 1][0]
         # return {"prediction": prediction}
    prediction = model.predict(X)
    prediction_list = prediction.tolist()
    return JSONResponse(content={"prediction": prediction_list})

