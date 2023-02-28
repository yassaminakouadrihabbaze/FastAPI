from keycloak import KeycloakOpenID

keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
                                 client_id="myapp",
                                 realm_name="yassaminakh",
                                 client_secret_key="")
