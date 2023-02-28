from fastapi import APIRouter, Depends
from requests import Session
from app.database import get_db
from app.modules.user.model import User

from app.modules.user.user_ro import UserRo
from app.modules.user.user_service import UserService


user_router = APIRouter()

@user_router.post('/users')
def create_user(payload: UserRo, db: Session = Depends(get_db)):
 user_service = UserService(db)
 created_user = user_service.create_user(payload)
 return created_user
