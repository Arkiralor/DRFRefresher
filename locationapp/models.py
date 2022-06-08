from django.db import models
from django.template.defaultfilters import slugify

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
    name = models.CharField(max_length=50, unique=True)
    common_name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    icann = models.CharField(max_length=7, blank=True, null=True)
    isd = models.CharField(max_length=5, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        '''
        Extended save() method to create a slug for the story.
        '''
        if not self.id or not self.slug:
            self.slug = slugify(self.name)
        super(CountryModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ('-created_at',)


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
        if not self.id or not self.slug:
            self.slug = slugify(f"{self.city_town}-{self.district_county}-{self.state_province}-{self.country.name}")
        super(LocationModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.city_town

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        ordering = ('-created_at',)
        unique_together = ('city_town', 'district_county', 'state_province', 'country')

    @property
    def name(self):
        name = f"{self.city_town}, {self.district_county}, {self.state_province}, {self.country.name}"
        return name.title()
