from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()
app.title = "API School"
app.version = "0.0.1"

class Teacher(BaseModel):
    id: Optional[int] = None
    nombres : str = Field(max_length = 40)
    apellidos : str = Field(max_length = 40) 
    email : str = Field(max_length = 40) 
    edad : int = Field(ge=1, le=100)
    telefono : str = Field(min_length=10,max_length = 40)

    class Config:
        schema_extra = {
            "example": {
                "id": 987654321,
                "nombres":"Pepito Andres",
                "apellidos":"Perez Gonzales",
                "email":"paperez@gmail.com",
                "edad":20,
                "telefono":"3111111111"
            }
        }

class Student(BaseModel):
    id: Optional[int] = None
    nombres : str = Field(max_length = 40)
    apellidos : str = Field(max_length = 40) 
    email : str = Field(max_length = 40) 
    edad : int = Field(ge=1, le=2)
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

students = [
    {
        "id" : 1144108708,
        "nombres":"Johan Leonardo",
        "apellidos": "Suarez Ospina",
        "email" : "leonardosp039@gmail.com",
        "edad" : 23,
        "grado" : "110-A",
        "horario" : "1",
        "telefono" : "3115798485"
    },
    {
        "id" : 987654321,
        "nombres":"Raquel Victoria",
        "apellidos": "Padilla Castillo",
        "email" : "raquesvictoriapadilla@gmail.com",
        "edad" : 21,
        "grado" : "110-B",
        "horario" : "2",
        "telefono" : "3196947699"
    }
]

teachers = [
    {
        "id" : 321654987,
        "nombres" : "Julian",
        "apellidos" : "Ipia Capote",
        "email" : "JICapote@gmail.com",
        "edad" : 23,
        "telefono" : "3112587812"
    },
    {
        "id" : 123456789,
        "nombres" : "Andres Felipe",
        "apellidos" : "Blandon Mondragon",
        "email" : "AFBlandon@gmail.com",
        "edad" : 22,
        "telefono" : "3118467985"
    }    
]

credentials = [
    {
        "id" : 1144108708,
        "user" : "jlsuarez",
        "password":"0000"
    },
    {
        "id" : 987654321,
        "user" : "rqpadilla",
        "password":"1111"
    },
    {
        "id" : 123456789,
        "user" : "afblandon",
        "password":"2222"
    },
    {
        "id" : 321654987,
        "user" : "jicapote",
        "password":"3333"
    }
]


@app.get('/student', tags=['student'])
def get_students()->List[Student]:
    return JSONResponse(status_code=200, content=students)

@app.get('/student/', tags=['student'])
def get_students_by_id(id:int) -> Student:
    for item in students:
        if item["id"] == id:
            return JSONResponse(status_code=200,content=item)
    return JSONResponse(status_code=404,content="No se encontro informacion")

@app.get('/teacher', tags=['teacher'],response_model=List[Teacher],status_code=200)
def get_teachers()->List[Teacher]:
    return JSONResponse(status_code=200,content=teachers)

@app.get('/teacher/{id}', tags=['teacher'],response_model=Teacher,status_code=200)
def get_teachers_by_id(id:int)->Teacher:
    for item in teachers:
        if item["id"] == id:
            return JSONResponse(status_code=200,content=item)
    return JSONResponse(status_code=404, content="No se encontro profesor")

@app.post('/teacher', tags=['teacher'],response_model=dict,status_code=201)
def create_teacher(teacher: Teacher)-> dict:
    teachers.append(dict(teacher))
    print(teachers)
    return JSONResponse(status_code = 201, content={"message":"Se agrego un profesor"})

@app.put('/teacher/{id}',tags=['teacher'],response_model=dict,status_code=200)
def update_teacher(id:int,teacher:Teacher)->dict:
    for item in teachers:
        if item["id"]== id:
            item["nombres"] = teacher.nombres
            item["apellidos"] = teacher.apellidos
            item["email"] = teacher.email
            item["edad"] = teacher.edad
            item["telefono"] = teacher.telefono
    return JSONResponse(status_code=200,content={"message":"Se ha modificado el profesor"})

@app.delete("/teacher/{id}",tags=['teacher'],response_model=dict,status_code=200)
def delete_teacher(id:int,teacher:Teacher)->dict:
    for item in teachers:
        if item["id"] == id:
            teachers.remove(item)
    return JSONResponse(status_code=200,content={"message":"Se ha eliminado el profesor"})


