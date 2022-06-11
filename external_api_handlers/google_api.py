from os import environ
import requests
from locationapp.models import LocationModel
from external_api_handlers import logger


class GoogleMapsAPIHandler:
    """
    Class to handle API calls to Google Maps.
    """
    api_key = environ.get('GOOGLE_API_KEY', None)
    if not api_key:
        logger.error("Google API key not found.")
    if api_key:
        logger.info(f"API KEY initiated.")

    api_base_url = 'https://maps.googleapis.com/maps/api/'
    geocode_endpoint = 'geocode/json'
    distance_matrix_endpoint = 'distancematrix/json'

    params = {
        'key': api_key,
    }

    @classmethod
    def make_request(cls, endpoint=None, data=None, params=None):
        """
        Make a POST request to the Google Maps API.
        """
        if params:
            params = {
                **cls.params,
                **params
            }
        url = f'{cls.api_base_url}{endpoint}'

        logger.info(f'Making request to {url}')
        response = requests.post(
            url,
            params=params,
            json=data
        )
        logger.info(f"Response received from {url}: {response.status_code}")
        return response.json()

    @classmethod
    def get_city_geocode(cls, location: LocationModel):
        """
        Get the geocode for a city.
        """
        resp = {}
        params = {
            'address': f"{location.city_town} {location.state_province} {location.country.name}",
            'sensor': 'false',
            'region': location.country.country_code,
            'language': 'en-GB'
        }
        response = cls.make_request(cls.geocode_endpoint, params=params)
        logger.info(f"Response from Google Maps API: {response.get('status')}")
        if response.get('status') in ('OK', ):
            ## prithoo (issue_004): Raw reponse can be seen in 'test_data/gmaps_geocode.json'.
            ## If not found within your clone of the repository, ask me for the file.
            # if the response is valid, set the first result as the result.
            response = response.get('results')[0]
            ## Massage the response to be more useful.
            resp['location'] = response.get('formatted_address')
            resp['geometry'] = response.get('geometry')
            resp['place_id'] = response.get('place_id')
            return resp
        ## If the response is not valid, return the errors.
        resp['error_message'] = response.get('error_message')
        resp['status'] = response.get('status')
        return resp

    @classmethod
    def get_city_reverse_geocode(cls, geocode: dict = None):
        """
        Get the reverse geocode for a city.
        """
        resp = {}

        params = {
            'sensor': 'false',
            'language': 'en-GB'
        }

        if geocode.get('place_id', None):
            params['place_id'] = geocode.get('place_id')
        elif geocode.get('location', None):
            params['latlng'] = f"{geocode.get('location').get('lat')},{geocode.get('location').get('lng')}"

        response = cls.make_request(cls.geocode_endpoint, params=params)
        logger.info(f"Response from Google Maps API: {response.get('status')}")
        if response.get('status') in ('OK', ):
            ## prithoo (issue_004): Raw reponse can be seen in 'test_data/gmaps_reverse_geocode.json'.
            ## If not found within your clone of the repository, ask me for the file.
            # if the response is valid, set the first result as the result.
            response = response.get('results')[0]
            ## Massage the response to be more useful.
            resp['location'] = response.get('formatted_address')
            resp['place_id'] = response.get('place_id')
            return resp
        ## If the response is not valid, return the errors.
        resp['error_message'] = response.get('error_message')
        resp['status'] = response.get('status')
        return resp
