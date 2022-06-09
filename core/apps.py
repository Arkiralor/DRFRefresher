DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'django_crontab',
    'rest_framework',
    'rest_framework.authtoken',
]
CUSTOM_APPS = [
    'userapp.apps.UserappConfig',
    'storyapp.apps.StoryappConfig',
    'searchapp.apps.SearchappConfig',
    'index_app.apps.IndexAppConfig',
    'locationapp.apps.LocationappConfig',
]