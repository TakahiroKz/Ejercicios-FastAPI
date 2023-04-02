from fastapi import FastAPI
from config.database import session
from models.user import User as UserModel
from schemas.user import User as UserSchema
from middleware.error_handler import ErrorHandler
from sqlmodel import select
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()
app.title = 'School'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)

@app.get("/user",tags=['1.user'])
def get_users():
    db = session
    statement = select(UserModel)
    result = db.exec(statement).all()
    if not result:
        JSONResponse(status_code=200, content={'message':'No se encontraro usuarios'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.get('/user/{id}',tags=['1.user'])
def get_user(id:int):
    db = session
    statement = select(UserModel).where(UserModel.id == id)
    result = db.exec(statement).first()
    if not result:
        return JSONResponse(status_code=404,content={'message':'Usuario no encontrado'})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@app.get('/user/',tags=['1.user'])
def get_user_by_name(name:str):
    db = session
    statement = f"Select * from apolo.user where nombre1 like'%{name}%' or nombre2 like'%{name}%'"
    result = db.execute(statement).all()
    if not result:
        return JSONResponse(status_code=404, content={'message':'Usuario no encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.post('/user',tags=['1.user'],response_model=dict)
def create_user(User:UserSchema):
    db = session
    new_movie = UserModel(**User.dict())
    db.add(new_movie)
    db.commit()   
    db.close() 
    return JSONResponse(status_code=201,content="Usuario Creado")

@app.put('/user', tags=['1.user'])
def update_user(id, data:UserModel):
    db = session
    statement = f"select * from apolo.user where id={id}"
    user = db.execute(statement).first()
    if not user:
        return JSONResponse(status_code=404, content="Usuario no encontrado para actualizar")
    user.id = data.id
    user.nombre1 = data.nombre1
    user.nombre2 = data.nombre2
    user.apellido1 = data.apellido1
    user.apellido2 = data.apellido2
    user.telefono = data.telefono
    user.correo = data.correo
    user.rol = data.rol
    user.rh = data.rh
    user.password = data.password
    user.direccion = data.direccion
    db.commit()
    return JSONResponse(status_code=200,content={'message:':'Se ha modificado el usuario'})

@app.delete('/user',tags=['1.user'])
def delete_user(id:int):
    db = session
    statement = select(UserModel).where(UserModel.id == id)
    result = db.exec(statement).first()
    if not result:
        return JSONResponse(status_code=404, content="Usuario no encontrado para eliminar")
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200,content={'message:':'Se ha eliminado el usuario'})