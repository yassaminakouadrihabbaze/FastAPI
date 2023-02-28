from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.patient.patient_model import Patient 
from app.modules.patient.patient_dao import PatientDAO
from app.modules.patient.patient_dto import PatientCreateDTO
from app.modules.patient.patient_ro import PatientRo
from app.modules.patient.patient_services import PatientService
from app.modules.user.model import User
from app.modules.user.user_dao import UserDao
from app.modules.user.user_ro import UserRo
from fastapi.encoders import jsonable_encoder
class UserService:
    def __init__(self, db: Session):
        self.user_dao = UserDao(db)
        self.patient_service = PatientService(db)
    def create_user(self, payload: UserRo) -> any:
        # patient = Patient(
        #     # patient_dto.dict()
        #     name=patient_dto.name,
        #     age=patient_dto.age,
        #     email=patient_dto.email,
        #     phone_number=patient_dto.phone_number
        # )
        user = User(
             name = payload.name,
            email = payload.email,
            usertype = payload.usertype
        )
        created_user =  self.user_dao.create(obj = user)
        print('created user',jsonable_encoder(created_user))
        if(payload.usertype == 'patient'):
            patient = PatientRo(user_id=user.id,phone_number=payload.patient_data.phone_number)
            created_patient = self.patient_service.create_patient(patient_ro=patient)
        yy = jsonable_encoder(created_user)
        return {"user":yy,"patient": created_patient}


    # def get_patient_with_id(self, patient_id: int ) -> Patient:
    #     patient = self.patient_dao.get_by_id(patient_id)
    #     print('this is our patiennnnnnnnnnnnnnnnnnnnt',patient)
    #     if patient is None:
    #         raise HTTPException(status_code=404, detail="Patient not found")
    #     return patient

    # def update_patient(self,id:int ,payload: PatientCreateDTO) -> Patient:
    #     fetched_patient = self.patient_dao.get_by_id(id)
    #     payload = payload.dict()
    #     if not fetched_patient:
    #         raise HTTPException(status_code=404, detail="patient with is : {id} does not exist ")
    #     updated_patient = self.patient_dao.update(fetched_patient,**payload)
    #     if not updated_patient:
    #         raise HTTPException(status_code=404, detail="Update failed ")
    #     return updated_patient