from topper.settings.base import *

DEBUG = True

# This will be the super user credentials used to login to the Django Admin page
SUPERUSER = {
    'name': 'admin',
    'email': 'admin@example.com',
    'password': 'pass'
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'pass',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

# Celery
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bvzh&txe6xd&()dd#fbr6h)8&!xq^229)dev-u*^df!yj)7u-!'
