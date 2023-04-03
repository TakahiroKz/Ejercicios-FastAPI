from models.user import User as UserModel
from sqlmodel import select
from schemas.user import User as UserSchema

class UserService():
    def __init__(self,db) -> None:
        self.db = db

    def get_users(self):
        statement = f"select * from apolo.user"
        result = self.db.execute(statement).all()
        return result
    
    def get_user(self,id:int):
        statement = f"select * from apolo.user where id = {id}"
        result = self.db.execute(statement).first()
        return result

    def get_user_by_name(self,name:str):
        statement = f"Select * from apolo.user where nombre1 like'%{name.capitalize()}%' or nombre2 like'%{name.capitalize()}%'"
        result = self.db.execute(statement).all()
        return result

    def create_user(self,user:UserSchema):
        newUser = UserModel(**user.dict())
        self.db.add(newUser)
        self.db.commit()
        return
    
    def update_user(self,id:int,data:UserSchema):
        user = self.db.query(UserModel).filter(UserModel.id == id).first()
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
        self.db.commit()
        return

    def delete_user(self,id:int):
        user = self.db.query(UserModel).filter(UserModel.id == id).first()
        self.db.delete(user) 
        self.db.commit()
        return
    
    