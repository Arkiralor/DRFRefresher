from django.db.models.signals import post_save, post_delete, m2m_changed

from locationapp.models import CountryModel, LocationModel
from locationapp import logger


class CountryModelSignalReciever:
    """
    Class to store all signals used in the locationapp.
    """
    model = CountryModel

    @classmethod
    def country_created(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a country is created.
        """
        request = kwargs.get('request')
        if created:
            logger.info(f"Country: {instance.name} created.")

    @classmethod
    def country_updated(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a country is updated.
        """
        request = kwargs.get('request')
        if not created:
            logger.info(f"Country {instance.name} updated.")

    @classmethod
    def country_deleted(cls, sender, instance, **kwargs):
        """
        Signal to send when a country is deleted.
        """
        logger.info(f"Country {instance.name} deleted.")


post_save.connect(receiver=CountryModelSignalReciever.country_created, sender=CountryModelSignalReciever.model)
post_save.connect(receiver=CountryModelSignalReciever.country_updated, sender=CountryModelSignalReciever.model)
post_delete.connect(receiver=CountryModelSignalReciever.country_deleted, sender=CountryModelSignalReciever.model)


class LocationModelSignalReciever:
    """
    Class to store all signals used in the locationapp.
    """
    model = LocationModel

    @classmethod
    def location_created(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a location is created.
        """
        if created:
            logger.info(f"Location '{instance.city_town}, {instance.country.name}' created.")

    @classmethod
    def location_updated(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a location is updated.
        """
        if not created:
            logger.info(f"Location '{instance.city_town}, {instance.country.name}' updated.")

    @classmethod
    def location_deleted(cls, sender, instance, **kwargs):
        """
        Signal to send when a location is deleted.
        """
        logger.info(f"Location '{instance.city_town}, {instance.country.name}' deleted.")


post_save.connect(receiver=LocationModelSignalReciever.location_created, sender=LocationModelSignalReciever.model)
post_save.connect(receiver=LocationModelSignalReciever.location_updated, sender=LocationModelSignalReciever.model)
post_delete.connect(receiver=LocationModelSignalReciever.location_deleted, sender=LocationModelSignalReciever.model)