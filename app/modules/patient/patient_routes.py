from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.modules.patient.patient_dao import PatientDAO
from app.modules.patient.patient_model import Patient
from app.modules.patient.patient_dto import PatientCreateDTO
from app.modules.patient.patient_services import PatientService

patient_router = APIRouter()

# def get_patient_service() -> PatientService:
#     return PatientService()

@patient_router.post('/patients')
    # patient_service = PatientService(db)
def create_patient(patient_dto: PatientCreateDTO, db: Session = Depends(get_db) ):
    patient_service = PatientService(db)
    # patient_dao = PatientDAO(db)
    created_patient = patient_service.create_patient(patient_dto)
    return created_patient

@patient_router.get('/patients')
def get_all_patients(db: Session = Depends(get_db)):
    patient_service = PatientService(db)
    return patient_service.patient_dao.get_all()

# class GetPatientDto(BaseModel):
#      id: int 
#      def __init__(self,patient: Patient):
#         self.id = patient.id

@patient_router.get('/patients/{id}')
def get_patient_with_id(id: int, db: Session = Depends(get_db)):
    patient_service = PatientService(db)
    result = patient_service.get_patient_with_id(id)
    return result

@patient_router.put('/patients/{id}')
def update_patient_with_id(id: int,payload: PatientCreateDTO, db: Session = Depends(get_db)):
    patient_service = PatientService(db)
    result = patient_service.update_patient(id,payload)
    return result




