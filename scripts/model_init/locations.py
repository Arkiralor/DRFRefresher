from locationapp.models import CountryModel, LocationModel
from locationapp.serializers import LocationModelSerializer
from scripts import logger
from django.db.models import Q
import pandas as pd

def add_locations():
    """
    Add locations to the database.
    """
    logger.info("Creating all first 100 locations...")
    
    
    df = pd.read_csv("scripts\model_init\data\cities_init.csv")
    logger.info(f"Retrieved {len(df)} locations.")

    list_of_locations = df.to_dict(orient='records')

    for location in list_of_locations:
        logger.info(f"Raw location: {location}")
        country = location.get('country_name')
        cc = location.get('country_code')
        country_obj = CountryModel.objects.filter(
                Q(name=country) 
                & Q(country_code=cc)
            ).first()
        location['country'] = country_obj.id
        del location['country_code']
        del location['country_name']
        logger.info(f"Formatted location: {location}")

        serialized = LocationModelSerializer(data=location)
        if serialized.is_valid():
            serialized.save()
        else:
            logger.error(f"Error creating Location: {serialized.errors}")

    logger.info("Finished creating all locations.")


if __name__ == "__main__":
    add_locations()