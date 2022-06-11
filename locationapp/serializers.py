from rest_framework.serializers import ModelSerializer
from locationapp.models import CountryModel, LocationModel


class CountryModelSerializer(ModelSerializer):
    class Meta:
        model = CountryModel
        fields = '__all__'


class LocationModelSerializer(ModelSerializer):
    class Meta:
        model = LocationModel
        fields = '__all__'
