
from typing import Optional
from sqlmodel import Field, SQLmodel


class Student(BaseModel):
    id: Optional[int] = None
    nombres : str = Field(max_length = 40)
    apellidos : str = Field(max_length = 40) 
    email : str = Field(max_length = 40) 
    edad : int = Field(ge=1, le=100)
    grado: str = Field(min_length=1,max_length = 5)
    horario:str = Field(min_length=1,max_length=1)
    telefono : str = Field(min_length=9,max_length = 15)

    class Config:
        schema_extra = {
            "example": {
                "id": 987654321,
                "nombres":"Pepito Andres",
                "apellidos":"Perez Gonzales",
                "email":"paperez@gmail.com",
                "edad":20,
                "grado":"110-A",
                "horario": "1",
                "telefono":3111111111
            }

        }

