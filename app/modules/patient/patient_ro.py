from typing import Optional
from pydantic import BaseModel


class PatientRo(BaseModel):
    phone_number : str
    user_id : Optional[int]
   