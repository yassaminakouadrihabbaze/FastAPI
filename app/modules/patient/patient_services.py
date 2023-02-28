from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.patient.patient_model import Patient 
from app.modules.patient.patient_dao import PatientDAO
from app.modules.patient.patient_dto import PatientCreateDTO
from app.modules.patient.patient_ro import PatientRo


class PatientService:
    def __init__(self, db: Session):
        self.patient_dao = PatientDAO(db)
    
    def create_patient(self, patient_ro: PatientRo) -> Patient:
        # patient = Patient(
        #     # patient_ro.dict()
        #     name=patient_ro.name,
        #     age=patient_ro.age,
        #     email=patient_ro.email,
        #     phone_number=patient_ro.phone_number
        # )
        patient = Patient(**patient_ro.dict())
        return self.patient_dao.create(patient)

    def get_patient_with_id(self, patient_id: int ) -> Patient:
        patient = self.patient_dao.get_by_id(patient_id)
        print('this is our patiennnnnnnnnnnnnnnnnnnnt',patient)
        if patient is None:
            raise HTTPException(status_code=404, detail="Patient not found")
        return patient

    def update_patient(self,id:int ,payload: PatientCreateDTO) -> Patient:
        fetched_patient = self.patient_dao.get_by_id(id)
        payload = payload.dict()
        if not fetched_patient:
            raise HTTPException(status_code=404, detail="patient with is : {id} does not exist ")
        updated_patient = self.patient_dao.update(fetched_patient,**payload)
        if not updated_patient:
            raise HTTPException(status_code=404, detail="Update failed ")
        return updated_patient