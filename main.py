from db.client_db import ClientInDB
from db.client_db import update_client, get_client, database_clients
from db.user_db import UserInDB
from db.user_db import get_user, database_users
from db.purchase_db import PurchaseInDB
from db.purchase_db import get_purchase, database_purchases
from db.product_db import  ProductInDB
from db.product_db import get_product, update_product, database_products

from models.client_models import ClientSearch, ClientIn, ClientOut
from models.user_models import UserIn, UserOut
from models.purchase_models import PurchaseSearch, PurchaseIn, PurchaseOut
from models.product_models import ProductSearch, ProductIn, ProductOut

import datetime

from fastapi import FastAPI, HTTPException

api = FastAPI()

#listar clientes
@api.get("/clients/")
async def get_all_clients():
    return database_clients

#Consultar Cliente
@api.get("/client/search/")
async def search_client(client_search: ClientSearch):
    client_in_db = get_client(client_search.cedula)
    if client_in_db == None:
        return {"El cliente no existe"}
    if client_in_db.cedula == client_search.cedula:
        return client_in_db

#Actualizar Cliente
@api.put("/client/update/")
async def update_client(client_in_db: ClientInDB):
    database_clients.update({client_in_db.cedula:client_in_db})
    return database_clients[client_in_db.cedula]

#Agregar Cliente
@api.post("/client/new/")
async def add_client(client_in_db: ClientInDB):
    if client_in_db.cedula not in database_clients:
        database_clients[client_in_db.cedula]=client_in_db
        return {"El cliente fue creado con exito"}
    else:
        return {"El cliente ya existe"}

#Eliminar Cliente
@api.post("/client/delete/")
async def delete_client(client_in_db: ClientSearch):
    try:
        if database_clients[client_in_db.cedula]:
            database_clients.pop(client_in_db.cedula)
            return {"El cliente fue borrado con exito"}
    except:
        return {"El cliente que intenta borrar no existe"}

#Verificar usuario
@api.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Usuario o contraseña incorrectos"}
    return {"¡Acceso exitoso! ¡Bienvenido!"}

#Consultar Compra
@api.get("/purchase/search/")
async def search_purchase(purchase_search: PurchaseSearch):
    purchase_in_db = get_purchase(purchase_search.id_compra)
    if purchase_in_db == None:
        return {"La compra no existe"}
    if purchase_in_db.id_compra == purchase_search.id_compra:
        return purchase_in_db

#Agregar Compra
@api.post("/purchase/new/")
async def update_purchase(purchase_in_db: PurchaseInDB):
    if purchase_in_db.id_compra not in database_purchases:
        database_purchases[purchase_in_db.id_compra]=purchase_in_db
        return {"La compra fue creada con exito"}
    else:
        return {"La compra ya existe"}

#Consultar Producto
@api.get("/product/search/")
async def search_product(product_search: ProductSearch):
    product_in_db = get_product(product_search.codigo_producto)
    if product_in_db == None:
        return {"El producto no se encuentra en el inventario"}
    if product_in_db.codigo_producto== product_search.codigo_producto:
        return product_in_db

#Actualizar Product
@api.put("/product/update/")
async def update_product(product_in_db: ProductInDB):
    database_products.update({product_in_db.codigo_producto:product_in_db})
    return database_products[product_in_db.codigo_producto]

#Agregar Product
@api.post("/product/new/")
async def add_product(product_in_db: ProductInDB):
    if product_in_db.codigo_producto not in database_products:
        database_products[product_in_db.codigo_producto]=product_in_db
        return {"El producto fue añadido al inventario"}
    else:
        return {"El producto ya está en el inventario"}

#Eliminar Product
@api.post("/product/delete/")
async def delete_product(product_in_db: ProductSearch):
    try:
        if database_products[product_in_db.codigo_producto]:
            database_products.pop(product_in_db.codigo_producto)
            return {"El producto fue removido del inventario"}
    except:
        return {"El producto que intenta borrar no está en el inventario"}
