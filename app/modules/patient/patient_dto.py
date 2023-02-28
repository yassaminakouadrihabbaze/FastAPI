from datetime import datetime
from pydantic import BaseModel

class PatientCreateDTO(BaseModel):
    name: str
    age: int
    email: str = None
    phone_number: str