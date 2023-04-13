# from aiohttp import request
from fastapi import Request
from fastapi import APIRouter, FastAPI, Depends, HTTPException, Header
import httpx
from keycloak import KeycloakOpenID
from sqlalchemy import null

from app.authentificator.login import LoginDto
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

keycloak_router = APIRouter()

security = HTTPBearer()

keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
                                 client_id="myapp",
                                 realm_name="yassaminakh",
                                 client_secret_key="")

# async def get_user(authorization: str = Header(...)):
#     token = keycloak_openid.introspect_token(token=authorization)
#     if token.get("active"):
#         user_info = await keycloak_openid.userinfo(authorization)
#         if user_info:
#             return user_info
#     raise HTTPException(status_code=401, detail="Invalid authentication credentials")

# async def get_user(authorization: str = Header(None)):
#     if authorization is None:
#         raise HTTPException(status_code=401, detail="Authorization header required")
#     try:
#         print('11111111111')
#         token = authorization.split()[0]
#         print('222222222222222')
#         print('hiiiiiiiiiiiiiiiiiiiii',token)
#         user_info = await keycloak_openid.userinfo(token)
#         print('3333333333333333')
#         return user_info
#     except Exception as e:
#         raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    

# import re

# async def get_user(authorization: str = Header(None)):
#     if authorization is None:
#         raise HTTPException(status_code=401, detail="Authorization header required")
#     try:
#         token_match = re.match("^Bearer\s(.+)$", authorization)
#         if token_match is None:
#             raise HTTPException(status_code=401, detail="Invalid authentication credentials")
#         token = token_match.group(1)
#         user_info = await keycloak_openid.userinfo(token)
#         return user_info
#     except Exception as e:
#         raise HTTPException(status_code=401, detail="Error retrieving user info")

# async def extract_information_from_token(token: str) -> dict:
#     userinfo_url = "http://localhost:8080/auth/realms/yassaminakh/protocol/openid-connect/userinfo"
#     headers = {"Authorization": f"Bearer {token}"}
#     response = requests.get(userinfo_url, headers=headers)
#     return response


# async def get_user_info(token: str ):
#     async with httpx.AsyncClient() as client:
#         response = await client.get(
#             "http://localhost:8080/auth/realms/yassaminakh/protocol/openid-connect/userinfo",
#             headers={"Authorization": f"Bearer {'token'}"}
#         )
#         user_info = await response.json()
#         return user_info
async def get_user(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        token = request.headers.get("Authorization")
        print('tooooooooooooooooken',token)
        async with httpx.AsyncClient() as client:
         response = await client.get(
            "http://localhost:8080/auth/realms/yassaminakh/protocol/openid-connect/userinfo",
            headers={"Authorization": token},
                         )
         user_info =  response.json()
         if "sub" in user_info:
            return user_info
         return null
    except :
        raise HTTPException(status_code=401, detail="Error retrieving user info")
    
# async def get_user_info(token: str):
#     print('tooooooooooooooooken',token)
#     async with httpx.AsyncClient() as client:
#         response = await client.get(
#             "http://localhost:8080/auth/realms/yassaminakh/protocol/openid-connect/userinfo",
#             headers={"Authorization": token},
#         )
#         user_info =  response.json()
#         return user_info






    
@keycloak_router.post("/get_token")
async def get_token(payload: LoginDto):
    token = keycloak_openid.token(payload.username, payload.password)
    return token


# @keycloak_router.post("/logout")
# async def get_token(request: Request):
#     # if user in None: 
#     #     raise HTTPException(status_code=401, detail= "Not Authentified !!!!")
#     token =  request.headers.get("Authorization")
#     print('heeeeeeeeeeeeeders',request.headers)
#     print("toooooooooooooken",token)
#     keycloak_openid.logout(token)
#     return {"message": " suuccesful logout"} 

@keycloak_router.post("/logout")
async def get_token(request: Request):
    token = request.headers.get("Authorization")
    print("toooooooooooooooooken",token)
    if token is not None:
        token = token.split()[1]  # Extract the token from the header
        keycloak_openid.logout(token)
        return {"message": "successful logout"}
    else:
        raise HTTPException(status_code=401, detail="Not authenticated")


@keycloak_router.get("/protectiied")
async def protected_route(user: dict = Depends(get_user)):
    print('hiiiiiiiiiiiiiii',user)
    if user is None: 
        raise HTTPException(status_code=401, detail="invalid user token , not authentified!!")
    # we will do me and wlidi some work or instractions here
    return {"message": "This is a protected route and you have the right to access congratulations ;)", "user": user}

@keycloak_router.get("/protectiiied")
async def get_user_info(request: Request):
    token = request.headers.get("Authorization")
    print('tooooooooooooooooken',token)
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "http://localhost:8080/auth/realms/yassaminakh/protocol/openid-connect/userinfo",
            headers={"Authorization": token},
        )
        user_info =  response.json()
        return user_info
