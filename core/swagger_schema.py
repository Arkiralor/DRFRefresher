from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="DRF Refresher API",
        default_version='v0.7',
        description="A basic django apllication used to refresh up on core concepts of Django and Django Restframework.",
        terms_of_service="",
        contact=openapi.Contact(email="prithoo11335@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)