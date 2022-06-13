from django.contrib import admin
from locationapp.models import CountryModel, LocationModel


@admin.register(CountryModel)
class CountryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'internet_tld', 'calling_code', 'created_at')
    search_fields = ('name', 'official_name', 'internet_tld', 'calling_code')
    list_filter= ('country_region',)
    ordering = ('name',)


@admin.register(LocationModel)
class LocationModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_town', 'country', 'created_at')
    search_fields = ('city_town', 'district_county',
                     'state_province', 'country__name')
    ordering = ('city_town', 'country__name')
    raw_id_fields = ('country',)
    list_filter = ('country__country_region', 'country__name',)
