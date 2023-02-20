from fastapi import FastAPI, Body, Path, Query

app = FastAPI()
app.title = "API School"
app.version = "0.0.1"

students = [
    {
        "identificacion" : 1144108708,
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
        "identificacion" : 123456789,
        "nombres" : "Andres Felipe",
        "apellidos" : "Blandon Mondragon",
        "email" : "leonardosp039@gmail.com",
        "edad" : 22,
        "telefono" : "3118467985"
    },
    {
        "identificacion" : 321654987,
        "nombres" : "Julian",
        "apellidos" : "Ipia Capote",
        "email" : "JICapote@gmail.com",
        "edad" : 23,
        "telefono" : "3112587812"
    }
]


@app.get('/student', tags=['student'])
def get_students(id:int):

    return id

@app.get('/teacher/{id}', tags=['teacher'])
def get_teachers(id:int):

    return id