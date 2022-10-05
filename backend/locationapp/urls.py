from django.urls import path
from locationapp.apis import CountryAPI, IndividualCountryAPI, LocationAPI, IndividualLocationAPI, \
    GetLocationCodeAPI

urlpatterns = [
    path('location/', LocationAPI.as_view(), name='location_list'),
    path('location/<slug:slug>', IndividualLocationAPI.as_view(),
         name='location_detail'),
    path('country/all', CountryAPI.as_view(), name='country_list'),
    path('country/<slug:slug>/',
         IndividualCountryAPI.as_view(), name='country_detail'),
    path('code/', GetLocationCodeAPI.as_view(), name='get_geocode'),
]
