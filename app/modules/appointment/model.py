# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from app.database import Base
# from app.modules.doctor.model import Doctor
# # Base = declarative_base()


# class Appointment(Base):
#     __tablename__ = 'appointments'
#     id = Column(Integer, primary_key=True)
#     date = Column(String)
#     time = Column(String)
#     status = Column(String)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship('User', back_populates='appointments')
#     doctor_id = Column(Integer, ForeignKey('doctors.id'))
#     doctor = relationship('Doctor', back_populates='appointments')
#     patient_id = Column(Integer, ForeignKey('patients.id'))
#     patient = relationship('Patient', back_populates='appointments')

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.modules.doctor.model import Doctor
# from app.modules.patient.patient_model import Patient
# from app.modules.doctor.model import Doctor
# from app.modules.patient.patient_model import Patient


class Appointment(Base):
    # def __init__(self, date, time, status, user_id, doctor_id, patient_id):
    #     from app.modules.user.model import User
    #     from app.modules.doctor.model import Doctor
    #     from app.modules.patient.patient_model import Patient
    #     self.date = date
    #     self.time = time
    #     self.status = status
    #     self.user_id = user_id
    #     self.doctor_id = doctor_id
    #     self.patient_id = patient_id
    #     self.user = User.query.get(user_id)
    #     self.doctor = Doctor.query.get(doctor_id)
    #     self.patient = Patient.query.get(patient_id)    

    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    time = Column(String)
    status = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='user_appts')
    patient_id = Column(Integer, ForeignKey('patients.id'))
    patient = relationship('Patient',back_populates='patient_appts',uselist=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    doctor = relationship('Doctor',back_populates='doctor_appts',uselist=False)

    # doctor_id = Column(Integer, ForeignKey('doctors.id'))
    # doctor = relationship(Doctor, back_populates='appointments')
    # patient = relationship('Patient', back_populates='appointments')

