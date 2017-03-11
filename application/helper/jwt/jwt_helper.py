from jwt import encode
from jwt import decode

JWT_SECRET_KEY = 'FAf3f2BB3@5!#gaw'

def jwt_encode(data, expire_timestamp=None):
    if expire_timestamp is not None:
        data['ext'] = expire_timestamp
    return encode(data, JWT_SECRET_KEY, algorithm='HS512')

def jwt_decode(token):
    return decode(token, JWT_SECRET_KEY)