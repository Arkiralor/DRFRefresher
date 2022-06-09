from django.contrib import admin
from locationapp.models import CountryModel, LocationModel

@admin.register(CountryModel)
class CountryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'common_name', 'internet_tld', 'calling_code', 'created_at')
    search_fields = ('name',)
    ordering = ('common_name',)


@admin.register(LocationModel)
class LocationModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_town', 'country', 'created_at')
    search_fields = ('city_town', 'district_county', 'state_province', 'country__name')
    ordering = ('-created_at',)
    raw_id_fields = ('country',)
