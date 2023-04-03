from jwt import encode, decode

def create_token(data:dict):
    token:str = encode(payload = data, key="FreakySchool",algorithm="HS256")
    return token

def validate_token(token:str):
    data:dict = decode(token,key="FreakySchool",algorithms=['HS256'])
    return data