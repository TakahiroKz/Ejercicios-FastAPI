from typing import Optional
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    __tablename__ = "user"
    __table_args__ = {"schema": "apolo"}
    id: Optional[int] = Field(default= None, primary_key=True)
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