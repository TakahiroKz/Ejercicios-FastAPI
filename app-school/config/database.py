import json
from sqlmodel import create_engine, Session

with open("config/credenciales.json") as archivo_credenciales:
    credenciales = json.load(archivo_credenciales)
    print(credenciales)

host = credenciales['host']
port = credenciales['port']
user = credenciales['user']
password = credenciales['password']
database = credenciales['database']

DATABASEURL = f'postgresql://{user}:{password}@{host}:{port}/{database}'
engine = create_engine(DATABASEURL,echo=True)

session = Session(engine)