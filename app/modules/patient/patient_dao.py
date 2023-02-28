from app.modules.patient.patient_model import Patient
from app.base.base_dao import BaseDAO


class PatientDAO(BaseDAO[Patient]):
    model = Patient
