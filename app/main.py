from fastapi import FastAPI
from app.modules.patient import patient_model 
from app.database import engine
from app.modules.patient.patient_routes import patient_router
from  app.authentificator.login import login_router
from app.modules.user.user_route import user_router

# patient_model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}

app.include_router(patient_router)
app.include_router(login_router)
app.include_router(user_router)


