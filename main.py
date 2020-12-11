from db.client_db import ClientInDB
from db.client_db import update_client, get_client, database_clients
from db.user_db import UserInDB
from db.user_db import get_user, database_users

from models.client_models import ClientSearch, ClientIn, ClientOut
from models.user_models import UserIn, UserOut 

import datetime

from fastapi import FastAPI, HTTPException

api = FastAPI()

#Verificar Cliente
@api.post("/client/auth/")
async def auth_client(client_in: ClientIn):
    client_in_db = get_client(client_in.cedula)
    if client_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    if client_in_db.nombres != client_in.nombres:
        return {"Autenticado": False}
    return {"Autenticado": True}

#Consultar Cliente
@api.get("/client/{cedula}/")
async def search_client(client_search: ClientSearch):
    client_in_db = get_client(client_search.cedula)
    if client_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    if client_in_db.cedula == client_search.cedula:
        return client_in_db

#Actualizar Cliente
@api.post("/client/{cedula}/")
async def search_client(client_in_db: ClientInDB):
    database_clients.update({client_in_db.cedula:client_in_db})
    return database_clients[client_in_db.cedula]

#Verificar usuario
@api.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Usuario o contraseña incorrectos"}
    return {"¡Acceso exioso! ¡Bienvenido!"}

