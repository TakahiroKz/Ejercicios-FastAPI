from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()
app.title = "API School"
app.version = "0.0.1"

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
        "identificacion" : 987654321,
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
        "id" : 123456789,
        "nombres" : "Andres Felipe",
        "apellidos" : "Blandon Mondragon",
        "email" : "leonardosp039@gmail.com",
        "edad" : 22,
        "telefono" : "3118467985"
    },
    {
        "id" : 321654987,
        "nombres" : "Julian",
        "apellidos" : "Ipia Capote",
        "email" : "JICapote@gmail.com",
        "edad" : 23,
        "telefono" : "3112587812"
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
def get_students()->list:
    return JSONResponse(status_code=200, content=students)

@app.get('/student/', tags=['student'])
def get_students_by_id(id:int) -> dict:
    for item in students:
        if item["id"] == id:
            return JSONResponse(status_code=200,content=item)
    return JSONResponse(status_code=404,content="No se encontro informacion")

@app.get('/teacher', tags=['teacher'])
def get_teachers() -> dict:
    return JSONResponse(status_code=200,content=teachers)

@app.get('/teacher/{id}', tags=['teacher'])
def get_teachers_by_id(id:int)->dict:
    for item in teachers:
        if item["id"] == id:
            return JSONResponse(status_code=200,content=item)
    return JSONResponse(status_code=404,content="No se encontro informacion")