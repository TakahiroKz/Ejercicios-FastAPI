from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    nombre1: str 
    nombre2: str 
    apellido1: str 
    apellido2: str
    telefono: int
    correo: str
    rol: int 
    rh: str 
    direccion: str
    password : str

    class Config:
        schema_extra = {
            "example":{
            "id": 0000000,
            "nombre1": "Aaaaa",
            "nombre2": "Bbbbb",
            "apellido1": "Ccccc",
            "apellido2": "Ddddd",
            "telefono": 300000000,
            "correo": "Abcd@gmail.com",
            "rol": 1,
            "rh":"A+",
            "direccion":"aaa#aaaa#aaa",
            'password' : 'str'
            }

        }