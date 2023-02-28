
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException ,Header
from fastapi_jwt_auth import AuthJWT
from app.authentificator.keyc_client import keycloak_openid
from datetime import datetime
from pydantic import BaseModel
from jose import jwt
from ..config import settings
from fastapi_jwt_auth import AuthJWT
from ..dotenv import secret_key

login_router = APIRouter()

class LoginDto(BaseModel):
    username: str
    password: str 
   

with open('private_key.pem', 'rb') as f:
    private_key = f.read()
@login_router.post("/login")
def login(payload: LoginDto):
    # Authenticate the user with Keycloak
    token  = keycloak_openid.token(payload.username, payload.password)  
    if token is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = jwt.encode(token, key=private_key, algorithm="RS256")
    return {"JWT_token": token}


with open('public_key.pem', 'rb') as f:
    public_key = f.read()

async def get_token_header(authorization: str = Header(...)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header is missing")
    token = authorization.split()[1]
    print(f"tooooooooooooooooooooooken :{token}")
    try:
        # print(f"SECRET_KEY: {private_key}")
        decoded_token = jwt.decode(token, key=public_key, algorithms="RS256")
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

# WE USE THE PREVIOUS FUNCTION IN THE ROUT'S THAT NEED'S TO BE BE AUTHED LIKE THE FOLOWING 
from fastapi import FastAPI, Depends

app = FastAPI()

@login_router.get("/protected")
async def protected_route(access_token: dict = Depends(get_token_header)):
    # Do something with the token
    print(access_token)
    return {"message": "You are authorized!","token": access_token}