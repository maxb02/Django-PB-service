
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fajud^0-mou3m9b^(ytmz!)6!kef=rbm21y7stbpfr8l!z-8er'


import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'pbservice',
#         'USER': 'django',
#         'PASSWORD': 'qweqwe',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }