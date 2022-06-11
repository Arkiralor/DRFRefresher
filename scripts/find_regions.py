from locationapp.models import CountryModel
from scripts import logger

def get_regions():
    """
    Get all regions from the database.
    """
    regions = CountryModel.objects.all().values_list('country_region', flat=True)
    regions = list(set(regions))
    logger.info(f"Regions: {regions}")

if __name__ == '__main__':
    get_regions()