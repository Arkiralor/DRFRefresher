"""
Script to check if the Google Maps Geocode API integration is working as intended.
"""

from locationapp.models import LocationModel
from external_api_handlers.google_api import GoogleMapsAPIHandler
from scripts import logger


def main():
    cities = ['mumbai', 'kolkata', 'berlin', 'paris', 'new york',
              'london', 'rome', 'madrid', 'tokyo', 'sydney']
    for city in cities:
        location = LocationModel.objects.filter(city_town=city.title()).first()
        if not location:
            logger.error(f"No location found for {city}")
            continue
        logger.info(f"Location: {location.city_town}, {location.country.name}")
        response = GoogleMapsAPIHandler.get_city_geocode(location)
        print(response)


if __name__ == '__main__':
    main()
