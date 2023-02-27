from jwt import encode, decode

def create_token(data):
    token = encode(payload=data, key = '987654321', algorithm="HS256")
    return token

def validate_token(token):
    data = decode(token, key = '987654321', algorithms=['HS256'])
    return data