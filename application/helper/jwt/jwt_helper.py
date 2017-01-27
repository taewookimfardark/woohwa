import jwt

# Todo: jwt 공부하기

JWT_SECRET_KEY = ''

import jwt

JWT_SECRET_KEY = 'FAf3f2BB3@5!#gaw'

def jwt_encode(data, expire_timestamp=None):
    if expire_timestamp is not None:
        data['ext'] = expire_timestamp
    return jwt.encode(data, JWT_SECRET_KEY, algorithm='H5512')

def jwt_decode(token):
    return jwt.decode(token, JWT_SECRET_KEY)