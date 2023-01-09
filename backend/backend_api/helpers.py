from django.conf import settings
import jwt

def jwt_encode_handler(payload):
    return jwt.encode(payload, settings.JWT_AUTH['JWT_SECRET_KEY'], algorithm=settings.JWT_AUTH['JWT_ALGORITHM']).decode('utf-8')

def jwt_decode_handler(token):
    return jwt.decode(token, settings.JWT_AUTH['JWT_SECRET_KEY'], algorithms=[settings.JWT_AUTH['JWT_ALGORITHM']])