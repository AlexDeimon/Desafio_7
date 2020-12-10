from pydantic import BaseModel

#Definición de los modelos de estado
class ClientIn(BaseModel):#Estado para autenticado
    cedula: str
    nombres: str

class ClientSearch(BaseModel):#Estado para consulta
    cedula: str

class ClientOut(BaseModel):
    cedula: str
    nombres: str
    apellidos: str
    email: str
    telefono: str