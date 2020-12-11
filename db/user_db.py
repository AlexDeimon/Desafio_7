from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str

database_users = Dict[str,UserInDB]

database_users={
    "DiegoSandoval":UserInDB(**{"username":"DiegoSandoval",
                                "password":"180999"}),
    "ValeriaGonzales":UserInDB(**{"username":"ValeriaGonzales",
                                "password":"8251012"}),
    "CamiloGarcia":UserInDB(**{"username":"CamiloGarcia",
                                "password":"2020827"}),
    "LauraBenavides":UserInDB(**{"username":"LauraBenavides",
                                "password":"1012202"}),
    "YesidBarragan":UserInDB(**{"username":"YesidBarragan",
                                "password":"2082910"})
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None