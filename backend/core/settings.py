from pathlib import Path
from os import environ, path, makedirs

from core.installations.apps import DEFAULT_APPS, THIRD_PARTY_APPS, CUSTOM_APPS
from core.installations.middleware import DEFAULT_MIDDLEWARE, THIRD_PARTY_MIDDLEWARE, CUSTOM_MIDDLEWARE

ENV_TYPE = environ.get('ENV_TYPE', 'prod').lower()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = environ['SECRET_KEY']

DEBUG = eval(environ['DEBUG'])


ALLOWED_HOSTS = environ['ALLOWED_HOSTS'].split(', ')


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
                'django.template.context_processors.media',
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
ENV_LOG_FILE = path.join(LOG_DIR, f'{ENV_TYPE}_root.log')
DJANGO_LOG_FILE = path.join(LOG_DIR, 'django.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'root_file': {
            'class': 'logging.FileHandler',
            'filename': ENV_LOG_FILE,
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
        'django_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': DJANGO_LOG_FILE,
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'local',
            'encoding': 'utf-8',
        }
    },
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s|%(asctime)s.%(msecs)d|%(name)s|%(module)s|%(funcName)s:%(lineno)s]    %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
        'local': {
            'format': '[%(asctime)s|%(name)s|%(module)s|%(funcName)s:%(lineno)s]    %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
    'loggers': {
        'root': {
            'handlers': ['console', 'root_file'],
            "level": 'INFO'
        },
        'django': {
            'handlers': ['console', 'django_file'],
            'level': 'INFO',
            'propagate': True
        },
    },
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        "Auth Token eg [token (JWT) ]": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }
}

LANGUAGE_CODE = environ['LANGUAGE_CODE']
TIME_ZONE = environ['TIME_ZONE']
USE_I18N = eval(environ['USE_I18N'])
USE_TZ = eval(environ['USE_TZ'])

AWS_ACCESS_KEY_ID = environ.get(('AWS_ACCESS_KEY_ID'))
AWS_SECRET_ACCESS_KEY = environ.get(('AWS_SECRET_ACCESS_KEY'))
AWS_STORAGE_BUCKET_NAME = environ.get(('AWS_STORAGE_BUCKET_NAME'))
AWS_REGION_NAME = environ.get("AWS_REGION_NAME")

USE_AWS_S3 = eval(environ.get("USE_AWS_S3", "True"))
if USE_AWS_S3:    
    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400"
    }
    # s3 static settings
    AWS_LOCATION = 'staticfiles'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'mediafiles'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = path.join(BASE_DIR, 'mediafiles')

STATICFILES_DIRS = (
    path.join(BASE_DIR, 'staticfiles'),
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'userapp.User'
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_WHITELIST = environ.get('CORS_ORIGIN_WHITELIST', '').split(', ')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = environ['EMAIL_HOST']
EMAIL_PORT = environ['EMAIL_PORT']
EMAIL_HOST_USER = environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = eval(environ['EMAIL_USE_TLS'])
EMAIL_USE_SSL = eval(environ['EMAIL_USE_SSL'])

OTP_ATTEMPT_LIMIT = int(environ.get('OTP_ATTEMPT_LIMIT', 10000))
OTP_ATTEMPT_TIMEOUT = int(environ.get('OTP_ATTEMPT_TIMEOUT', 0))

## Razorpay credentials:
RAZORPAY_KEY = environ.get('RAZORPAY_KEY_ID', None)
RAZORPAY_SECRET = environ.get('RAZORPAY_SECRET_KEY', None)

