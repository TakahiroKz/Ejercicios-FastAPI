from fastapi import FastAPI
from config.database import engine
from models.user import User as UserModel
from schemas.user import User as UserSchema
from middleware.error_handler import ErrorHandler
from sqlmodel import SQLModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from routers.user import user_routing
from routers.login import login_router

app = FastAPI()
app.title = 'School'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)
app.include_router(user_routing)
app.include_router(login_router)

SQLModel.metadata.create_all(engine)

