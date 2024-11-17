import jwt
import time
from django.conf import settings

def generate_jwt(user):
    timestamp = time.time() + 60*60*24*7
    return jwt.encode({"userid":user.p k, "exp":timestamp}, settings.SECRET_KEY).decode("utf-8")