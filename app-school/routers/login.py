from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Query,Path,Depends
from fastapi.encoders import jsonable_encoder
from config.database import session
from pydantic import BaseModel
from jwt_manager import create_token
from schemas.login import Login as LoginSchema
from services.user import UserService

login_router = APIRouter()

@login_router.post('/0.login',tags=['auth'],status_code=200)
def login(user:LoginSchema):
    db = session
    correo = user.email
    password = user.password
    result = UserService(db).get_user_by_email(correo)
    if not result:
        return JSONResponse(status_code=403, content={'message':'Correo Invalido'})

    result = UserService(db).check_user(correo, password)
    if result == False:
        return JSONResponse(status_code=503, content={'message':'Credenciales invalidas'})
    
    rol = UserService(db).get_rol(correo)
    userRol = user.dict()
    userRol['rol'] = rol[0]
    print(userRol)
    token:str = create_token(userRol)



    return JSONResponse(status_code=200, content=token)