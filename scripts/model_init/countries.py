from scripts import logger
from locationapp.models import CountryModel
from locationapp.serializers import CountryModelSerializer
import pandas as pd


def create_countries():
    """
    Creates all countries in the database.
    """
    logger.info("Creating all countries...")

    df = pd.read_csv("scripts\model_init\data\countries.csv")
    logger.info(f"Retrieved {len(df)} countries.")

    list_of_dicts = df.to_dict('records')
    logger.info(f"Converted Dataframe to list of json")

    for country in list_of_dicts:
        logger.info(f"Creating Country: {country.get('name')}.")
        serializer = CountryModelSerializer(data=country)

        if serializer.is_valid():
            serializer.save()
        else:
            logger.error(f"Error creating Country: {serializer.errors}")

    logger.info("Finished creating all countries.")


if __name__ == "__main__":
    create_countries()
