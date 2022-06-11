from django.db import models
from django.template.defaultfilters import slugify
from locationapp.model_choices import CountryModelChoice

import uuid


class CountryModel(models.Model):
    """
    Model to hold information about individual countries.
    """
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=128, unique=True,
                            default="Default Country Name", help_text="Common name of the country.")
    official_name = models.CharField(max_length=256, blank=True, null=True,
                                     help_text="Official name of the country as presented in legal documents.")
    slug = models.SlugField(max_length=256, null=True, blank=True,
                            help_text="Slug used to identify/route to the country.")
    country_code = models.CharField(
        max_length=10, blank=True, null=True, help_text="ISO 3166-1 alpha-2 country code.")
    country_region = models.CharField(
        max_length=128, 
        choices=CountryModelChoice.region_choices, 
        blank=True, 
        null=True, 
        help_text="Region of the country."
    )
    internet_tld = models.CharField(
        max_length=10, blank=True, null=True, help_text="Internet top level domain for the country")
    calling_code = models.CharField(
        max_length=10, blank=True, null=True, help_text="International Dialing Code for the country.")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        '''
        Extended save() method to create a slug for the story.
        '''
        self.slug = slugify(self.official_name)
        super(CountryModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ('name',)


class LocationModel(models.Model):
    """
    Model to hold information about cities/towns inside countries.
    """
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    city_town = models.CharField(max_length=50, blank=True, null=True)
    district_county = models.CharField(max_length=50, blank=True, null=True)
    state_province = models.CharField(max_length=50, blank=True, null=True)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        '''
        Extended save() method to create a slug for the story.
        '''
        self.slug = slugify(
                f"{self.city_town}-{self.district_county}-{self.state_province}-{self.country.name}")
        super(LocationModel, self).save(*args, **kwargs)

    def __str__(self):
        rep = f"{self.city_town}, {self.country.name}"
        return rep

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        ordering = ('country', 'city_town')
        unique_together = ('city_town', 'district_county',
                           'state_province', 'country')

    @property
    def name(self):
        name = f"{self.city_town}, {self.district_county}, {self.state_province}, {self.country.name}"
        return name.title()
