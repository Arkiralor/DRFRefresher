from os import environ
import requests
from locationapp.models import CountryModel, LocationModel
from external_api_handlers import logger

class GoogleMapsAPIHandler:
    """
    Class to handle API calls to Google Maps.
    """
    api_key = environ.get('GOOGLE_API_KEY')
    api_secret = environ.get('GOOGLE_API_SECRET')

    api_base_url = 'https://maps.googleapis.com/maps/api/'
    geocode_endpoint = 'geocode/json'
    reverse_geocode_endpoint = 'reversegeocode/json'
    distance_matrix_endpoint = 'distancematrix/json'

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f"Bearer {api_secret}"
    }
    params = {
        'address': None, 
        'components': None, 
        'bounds': None, 
        'region': None, 
        'language': None, 
        'result_type': None, 
        'location_type': None, 
        'latlng': None, 
        'place_id': None, 
        'key': None
    }
    
    @classmethod
    def make_request(cls, endpoint=None, data=None, params=None, headers=None):
        """
        Make a request to the Google Maps API.
        """
        params = {
            **cls.params,
            **params
        }
        headers = {
            **cls.headers,
            **headers
        }   
        url = f'{cls.api_base_url}{endpoint}'

        logger.info(f'Making request to {url}')
        response = requests.get(
            url, 
            params=params, 
            headers=cls.headers,
            json=data
        )
        if response.status_code in (200, 201):
            return response.json()
        else:
            return response.text

    @classmethod
    def get_city_geocode(cls, location:LocationModel):
        """
        Get the geocode for a city.
        """
        params = {
            'address': location.city_town,
            'components': {
                'administrative_area': location.state_province,
                'country': location.country.country_code,
                'region': location.country.country_region
                },
        }
        response = cls.make_request(cls.geocode_endpoint, params=params)
        
        if response.get('status_code') in ('OK', 'ZERO_RESULTS'):
            return response
        else:
            logger.warn(f'Error getting geocode for {location.city_town}, {location.country.name}')
            return None