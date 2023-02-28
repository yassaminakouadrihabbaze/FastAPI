# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# from app.modules.appointment.model import Appointment
# from app.modules.user.model import User
# # Base = declarative_base()

# class Doctor(User):
#     __tablename__ = 'doctors'
#     id = Column(Integer, ForeignKey('users.id'), primary_key=True)
#     specialty = Column(String)
#     appointments = relationship('Appointment', back_populates='doctor')
#     __mapper_args__ = {'polymorphic_identity': 'doctors'}

# # Appointment.doctor = relationship(Doctor, back_populates='appointments')

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# from app.modules.appointment.model import Appointment
from app.database import Base
# from app.modules.appointment.model import Appointment
# from ..user.model import User

# Base = declarative_base()

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    specialty = Column(String)
    user_id = Column(Integer,ForeignKey('users.id'), nullable=False)
    user = relationship('User', uselist=False,back_populates='user_doctor')
    doctor_appts = relationship('Appointment',uselist=True,back_populates='doctor')

    # user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # user = relationship('User', backref="doctors")
    # appointments = relationship('Appointment', back_populates='doctor')
    # __mapper_args__ = {'polymorphic_identity': 'doctors'}
    
# Appointment.doctor = relationship(Doctor, back_populates='appointments', lazy=True)