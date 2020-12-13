from typing import Dict
from pydantic import BaseModel

class ProductInDB(BaseModel):
    codigo_producto: str
    nombre_producto: str
    precio: str
    cantidad_disponible: str

database_products = Dict[str, ProductInDB]

#Base de datos ficticia
database_products = {
    "TV12345": ProductInDB(**{"codigo_producto":"TV12345",
                            "nombre_producto":"Televisor 65 pulg",
                            "precio":"2100000",
                            "cantidad_disponible":"666" }),

     "NV23415": ProductInDB(**{"codigo_producto":"NV23415",
                            "nombre_producto":"Nevecon Whirlpool",
                            "precio":"4600000",
                            "cantidad_disponible":"34" }),

     "LV45678": ProductInDB(**{"codigo_producto":"LV45678",
                            "nombre_producto":"Lavadora LG 18k",
                            "precio":"1400000",
                            "cantidad_disponible":"55" }),

     "MN12986": ProductInDB(**{"codigo_producto":"MN12986",
                            "nombre_producto":"Monitor LG 25 pulg",
                            "precio":"800000",
                            "cantidad_disponible":"120" }),

      "HM78546": ProductInDB(**{"codigo_producto":"HM78546",
                            "nombre_producto":"Horno microondas oster 20l",
                            "precio":"240000",
                            "cantidad_disponible":"70" })                                             
   
}

def get_product(codigo_producto: str):
    if codigo_producto in database_products.keys():
        return database_products[codigo_producto]
    else:
        return None

 def update_product(product_in_db: ProductInDB): 
    database_products[product_in_db.codigo_product] = product_in_db
    return product_in_db