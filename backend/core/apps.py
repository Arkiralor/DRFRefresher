DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg'
]
CUSTOM_APPS = [
    'userapp.apps.UserappConfig',
    'storyapp.apps.StoryappConfig',
    'searchapp.apps.SearchappConfig',
    'index_app.apps.IndexAppConfig',
    'locationapp.apps.LocationappConfig',
    'blacklist.apps.BlacklistConfig',
    'payment_app.apps.PaymentAppConfig'
]
