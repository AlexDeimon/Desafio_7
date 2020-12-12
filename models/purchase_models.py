from pydantic import BaseModel

#Definición de los modelos de estado
class PurchaseIn(BaseModel):#Estado para autenticado
    id_compra: str

class PurchaseSearch(BaseModel):#Estado para consulta
    id_compra: str

class PurchaseOut(BaseModel):
    id_compra: str
    cedula: str
    nombres: str
    apellidos: str
    codigo_producto: str
    producto: str
    precio_compra: str