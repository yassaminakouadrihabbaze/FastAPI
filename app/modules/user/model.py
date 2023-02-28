# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# from app.modules.appointment.model import Appointment
# from ...database import Base

# # Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     email = Column(String)
#     appointments = relationship('Appointment', back_populates='user', uselist=True, single_parent=True, cascade='all, delete-orphan', passive_deletes=True)
#     usertype = Column(String)
#     __mapper_args__ = {'polymorphic_identity': 'users', 'polymorphic_on': usertype}

# Appointment.user = relationship(User, back_populates='appointments')
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base
from app.modules.appointment.model import Appointment

# Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    # appointments = relationship('Appointment', back_populates='user', uselist=True, single_parent=True, cascade='all, delete-orphan', passive_deletes=True)
    usertype = Column(String,nullable=True)
    user_appts = relationship('Appointment', back_populates='user', uselist=True, single_parent=True, cascade='all, delete-orphan', passive_deletes=True)    # __mapper_args__ = {'polymorphic_identity': 'users', 'polymorphic_on': usertype}
    user_patient = relationship('Patient',back_populates='user',uselist=False)
    user_doctor = relationship('Doctor',back_populates='user',uselist=False)
# Appointment.user = relationship(User, back_populates='appointments')
