from pathlib import Path
from os import environ, path, makedirs

from core.apps import DEFAULT_APPS, THIRD_PARTY_APPS, CUSTOM_APPS
from core.middleware import DEFAULT_MIDDLEWARE, THIRD_PARTY_MIDDLEWARE, CUSTOM_MIDDLEWARE

env_type = environ.get('ENV_TYPE', 'dev').lower()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = environ['SECRET_KEY']

DEBUG = eval(environ['DEBUG'])


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]


INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + CUSTOM_APPS
MIDDLEWARE = DEFAULT_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE + CUSTOM_MIDDLEWARE

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ['PGDATABASE'],
        'HOST': environ['PGHOST'],
        'PORT': environ['PGPORT'],
        'USER': environ['PGUSER'],
        'PASSWORD': environ['PGPASSWORD'],
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

## Create directory for logs
LOG_DIR = path.join(BASE_DIR, 'logs/')
if not path.exists(LOG_DIR):
    makedirs(LOG_DIR)
LOG_FILE = path.join(LOG_DIR, f'{env_type}.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s|%(asctime)s.%(msecs)d|PROCESS:%(process)d|THREAD:%(thread)d|%(name)s|%(module)s|%(funcName)s|%(lineno)s]   %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
    'loggers': {
        'root': {
            'handlers': ['console', 'file'],
            "level": 'INFO'
        },
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    },
}

LANGUAGE_CODE = environ['LANGUAGE_CODE']
TIME_ZONE = environ['TIME_ZONE']
USE_I18N = eval(environ['USE_I18N'])
USE_TZ = eval(environ['USE_TZ'])

STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     path.join(BASE_DIR, 'static')
# ]
STATIC_ROOT = path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'userapp.User'
CORS_ALLOW_ALL_ORIGINS = True
