from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from os import environ

schema_view = get_schema_view(
    openapi.Info(
        title="DRF Refresher API",
        default_version='v0.7',
        description="A basic django apllication used to refresh up on core concepts of Django and Django Restframework.",
        terms_of_service="",
        contact=openapi.Contact(email=environ.get('LINKEDIN_PROFILE')),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
