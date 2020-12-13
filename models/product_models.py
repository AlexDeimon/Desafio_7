from pydantic import BaseModel

class ProductIn(BaseModel):
    codigo_producto: str

class ProductSearch(BaseModel):
    codigo_producto: str

class ProductOut(BaseModel):
    codigo_producto: str
    nombre_producto: str
    precio: str
    cantidad_disponible: str