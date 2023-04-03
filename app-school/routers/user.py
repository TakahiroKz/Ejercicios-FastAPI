from fastapi import APIRouter
from fastapi import Path, Query, Depends
from typing import List
from middleware.jwt_bearer import JWTBearer
from config.database import session
from models.user import User as UserModel
from schemas.user import User as UserSchema
from services.user import UserService
from sqlmodel import select
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

user_routing = APIRouter()

@user_routing.get("/user",tags=['1.user'],response_model=List[UserSchema])
def get_users():
    db = session
    result = UserService(db).get_users()
    if not result:
        JSONResponse(status_code=200, content={'message':'No se encontraro usuarios'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@user_routing.get('/user/{id}',tags=['1.user'])
def get_user(id:int):
    db = session
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404,content={'message':'Usuario no encontrado'})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@user_routing.get('/user/',tags=['1.user'])
def get_user_by_name(name:str):
    db = session    
    result = UserService(db).get_user_by_name(name)
    if not result:
        return JSONResponse(status_code=404, content={'message':'Usuario no encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@user_routing.post('/user',tags=['1.user'],response_model=dict)
def create_user(user:UserSchema):
    db = session
    id = user.id
    result = UserService(db).get_user(id)
    if result:
        return JSONResponse(status_code=500,content={'message':'Ya existe un registro con este ID'})
    UserService(db).create_user(user)
    return JSONResponse(status_code=201,content="Usuario Creado")

@user_routing.put('/user/{id}', tags=['1.user'])
def update_user(id:int, data:UserSchema):
    db = session
    user = UserService(db).get_user(id)
    if not user:
        return JSONResponse(status_code=404, content="Usuario no encontrado para actualizar")
    UserService(db).update_user(id,data)
    return JSONResponse(status_code=200,content={'message:':'Se ha modificado el usuario'})

@user_routing.delete('/user',tags=['1.user'])
def delete_user(id:int):
    db = session
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content="Usuario no encontrado para eliminar")
    UserService(db).delete_user(id)
    return JSONResponse(status_code=200,content={'message:':'Se ha eliminado el usuario'})