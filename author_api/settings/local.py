from .base import *

from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='kk9hq9+psl0%76ce00ba2rd9ohxf(l2lqn2i8b2!ik&po8_8px'
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

CSRF_TRUSTED_ORIGINS = ['http://localhost:8080','http://127.0.0.1:8080']
# email backend
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "info@authors_haven.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors Haven"