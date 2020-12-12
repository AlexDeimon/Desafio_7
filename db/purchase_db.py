from typing import Dict
from pydantic import BaseModel

class PurchaseInDB(BaseModel):
    id_compra: str
    cedula: str
    nombres: str
    apellidos: str
    codigo_producto: str
    producto: str
    precio_compra: str

database_purchases = Dict[str, PurchaseInDB]

#Base de datos ficticia
database_purchases = {
    "01": PurchaseInDB(**{"id_compra":"01",
                            "cedula":"11111",
                            "nombres":"Winston Leonard",
                            "apellidos":"Spencer Churchill",
                            "codigo_producto":"TV12345",
                            "producto":"Televisor 65 pulg",
                            "precio_compra":"2100000"}),

    "02": PurchaseInDB(**{"id_compra":"02",
                            "cedula":"22222",
                            "nombres":"Dwight David",
                            "apellidos":"Eisenhower",
                            "codigo_producto":"NV23415",
                            "producto":"Nevecon Whirlpool",
                            "precio_compra":"4600000"}),

    "03": PurchaseInDB(**{"id_compra":"03",
                            "cedula":"55555",
                            "nombres":"Kurt Arthur",
                            "apellidos":"Benno Student",
                            "codigo_producto":"LV45678",
                            "producto":"Lavadora LG 18k",
                            "precio_compra":"1400000"}),

    "04": PurchaseInDB(**{"id_compra":"04",
                            "cedula":"33333",
                            "nombres":"Omar Nelson",
                            "apellidos":"Bradley",
                            "codigo_producto":"MN12986",
                            "producto":"Monitor LG 25 pulg",
                            "precio_compra":"800000"}),

    "05": PurchaseInDB(**{"id_compra":"05",
                            "cedula":"44444",
                            "nombres":"Erwin Johannes",
                            "apellidos":"Eugen Rommel",
                            "codigo_producto":"HM78546",
                            "producto":"Horno microondas oster 20l",
                            "precio_compra":"240000"})
}

def get_purchase(id_compra: str):
    if id_compra in database_purchases.keys():
        return database_purchases[id_compra]
    else:
        return None