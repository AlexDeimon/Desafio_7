from typing import Dict
from pydantic import BaseModel

class ClientInDB(BaseModel):
    cedula: str
    nombres: str
    apellidos: str
    email: str
    telefono: str

database_clients = Dict[str, ClientInDB]

#Base de datos ficticia
database_clients = {
    "11111": ClientInDB(**{"cedula":"11111",
                            "nombres":"Winston Leonard",
                            "apellidos":"Spencer Churchill",
                            "email":"winston.churchill@gmail.com",
                            "telefono":"7893214568"}),

    "22222": ClientInDB(**{"cedula":"22222",
                            "nombres":"Dwight David",
                            "apellidos":"Eisenhower",
                            "email":"david.eisenhower@gmail.com",
                            "telefono":"3578521596"}),

    "33333": ClientInDB(**{"cedula":"33333",
                            "nombres":"Omar Nelson",
                            "apellidos":"Bradley",
                            "email":"omar.bradley@gmail.com",
                            "telefono":"4863217592"}),

    "44444": ClientInDB(**{"cedula":"44444",
                            "nombres":"Erwin Johannes",
                            "apellidos":"Eugen Rommel",
                            "email":"erwin.rommel@gmail.com",
                            "telefono":"5987432175"}),

    "55555": ClientInDB(**{"cedula":"55555",
                            "nombres":"Kurt Arthur",
                            "apellidos":"Benno Student",
                            "email":"kurt.student@gmail.com",
                            "telefono":"3574159845"})
}

def get_client(cedula: str):
    if cedula in database_clients.keys():
        return database_clients[cedula]
    else:
        return None

def update_client(client_in_db: ClientInDB):#Se recibe un dato client_in_db de tipo UserInDB
    database_clients[client_in_db.cedula] = client_in_db
    return client_in_db