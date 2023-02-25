from jwt import encode, decode

def create_token(data:dict)->str:
    token:str = encode(payload=data,key="987654321",algorithm="HS256")
    return token

def validate_token(token:str)->dict:
    data : dict = decode(token,key="987654321", algorithms=["HS356"])
    return data