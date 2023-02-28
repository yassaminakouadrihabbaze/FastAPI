from enum import Enum
from pydantic import BaseModel
from typing import Optional

from app.modules.patient.patient_ro import PatientRo

class UserType(str, Enum):
    doctor = 'doctor'
    patient = 'patient'

class UserRo(BaseModel):
    name: str
    email: str
    usertype: UserType 
    patient_data : Optional[PatientRo]
    # doctor_data : Optional[DoctorRo]