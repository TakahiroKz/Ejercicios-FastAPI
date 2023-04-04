from config.database import session
from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from services.user import UserService
from jwt_manager import validate_token,create_token



class JWTBearer(HTTPBearer):
    async def __call__(self, request:Request):
        db = session
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        email = data['email']
        password = data['password']
        rol= data['rol']
        if UserService(db).check_user(email,password):
            print("OK")
        else:
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")
            