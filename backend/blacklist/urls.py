from django.urls import path, include
from rest_framework import routers

from blacklist.apis import BlacklistedEmailViewSet, BlacklistedPhoneNumberViewSet, BlacklistedPasswordViewSet

router = routers.DefaultRouter()
router.register(r'blacklisted_email', BlacklistedEmailViewSet, basename='blacklisted_emails')
router.register(r'blacklisted_phone_number', BlacklistedPhoneNumberViewSet, basename='blacklisted_phone_numbers')
router.register(r'blacklisted_password', BlacklistedPasswordViewSet, basename='blacklisted_passwords')

urlpatterns = [
    path(r'apis/', include(router.urls)),
]

