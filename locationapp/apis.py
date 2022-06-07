from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from locationapp.models import CountryModel, LocationModel
from locationapp.serializers import CountryModelSerializer, LocationModelSerializer


class CountryModelViewSet(ModelViewSet):
    queryset = CountryModel.objects.all()
    serializer_class = CountryModelSerializer


class LocationModelViewSet(ModelViewSet):
    queryset = LocationModel.objects.all()
    serializer_class = LocationModelSerializer
