from db.client_db import ClientInDB
from db.client_db import update_client, get_client

from models.client_models import ClientSearch, ClientIn, ClientOut

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