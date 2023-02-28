# # from datetime import datetime
# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
# from sqlalchemy.orm import relationship
# # from app.modules.user.model import User
# from app.database import Base
# from app.modules.user.model import User 
# # Base = declarative_base()

# # class Patient(Base):
# #    __tablename__ = 'patients'

# #    id = Column(Integer, primary_key=True, index=True)
# #    name = Column(String(255))
# #    age = Column(Integer)
# #    email = Column(String(255), nullable=True)
# #    phone_number = Column(String(20))


# class Patient(User):
#     __tablename__ = 'patients'
#     id = Column(Integer, ForeignKey('users.id'), primary_key=True)
#     phone_number = Column(String)
#     appointments = relationship('Appointment', back_populates='patient')
#     __mapper_args__ = {'polymorphic_identity': 'patients'}

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.modules.user.model import User
from app.modules.appointment.model import Appointment
from app.database import Base

# Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    phone_number = Column(String)
    user_id = Column(Integer,ForeignKey('users.id'), nullable=False)
    user = relationship('User', uselist=False,back_populates='user_patient')
    # Patient_id = Column(Integer,ForeignKey('appointments.id') )
    patient_appts = relationship('Appointment',uselist=True,back_populates='patient')
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     user = relationship(User, backref="patients")
#     appointments = relationship('Appointment', back_populates='patient')
#     __mapper_args__ = {'polymorphic_identity': 'patients'}

# Appointment.patient = relationship(Patient, back_populates='appointments')