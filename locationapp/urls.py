from django.urls import path, include
from rest_framework import routers
from locationapp.apis import CountryModelViewSet, LocationModelViewSet

model_router = routers.DefaultRouter()
model_router.register(r'country', CountryModelViewSet)
model_router.register(r'location', LocationModelViewSet)

urlpatterns = [
    path('', include(model_router.urls)),
]