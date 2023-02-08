from .base import *

from .base import env

DJANGO_DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'DJANGO_SECRET_KEY', 
    default='kk9hq9+psl0%76ce00ba2rd9ohxf(l2lqn2i8b2!ik&po8_8px'
    )

ALLOWED_HOSTS = ["127.0.0.1", "localhost","0.0.0.0"]