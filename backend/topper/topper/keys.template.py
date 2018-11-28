import os

REDDIT = {
    'client_id': '',
    'client_secret': '',
    'password': '',
    'username': ''
}

POCKET_CASTS = {
    'username': '',
    'password': ''
}

# This will be the super user credentials used to login to the Django Admin page
SUPERUSER = {
    'name': '',
    'email': '',
    'password': ''
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

SECRET_KEY = ''
