from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer, SecurityScopes
from keycloak import KeycloakOpenID

app = FastAPI()

# Keycloak settings
# keycloak_openid = KeycloakOpenID(server_url="https://example.com/auth/",
#                                  client_id="your-client-id",
#                                  client_secret_key="your-client-secret",
#                                  realm_name="your-realm",
#                                  scopes=["openid"])

keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
                                 client_id="myapp",
                                 realm_name="yassaminakh",
                                 client_secret_key=""
                                )

oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="http://localhost:8080/auth/realms/your-realm/protocol/openid-connect/token",
                                             scopes={"openid": "OpenID Connect"})

# Authentication dependency
async def get_user(openid: KeycloakOpenID = Depends(keycloak_openid)):
    # Get the access token from the OAuth2AuthorizationCodeBearer
    token = await oauth2_scheme.__call__([])
    # Use the access token to extract user information
    user_info = await openid.userinfo(token)
    if user_info:
        return user_info
    raise HTTPException(status_code=401, detail="Invalid authentication credentials")

# Authorization dependency
async def has_access(scopes: SecurityScopes, openid: KeycloakOpenID = Depends(keycloak_openid)):
    # Get the access token from the OAuth2AuthorizationCodeBearer
    token = await oauth2_scheme.__call__([])
    # Use the access token to extract user roles
    user_roles = await openid.user_roles(token, "your-realm")
    for scope in scopes.scopes:
        if scope not in user_roles:
            raise HTTPException(status_code=403, detail="Forbidden")
    return True

# Protected routes
@app.get('/api/protected')
async def protected_route(user: dict = Depends(get_user), authorized: bool = Depends(has_access(scopes=["admin"]))):
    # The user has valid authentication and authorization
    return {"message": "This is a protected route"}

@app.get('/api/unprotected')
async def unprotected_route():
    # This route is not protected and does not require authentication or authorization
    return {"message": "This is an unprotected route"}
