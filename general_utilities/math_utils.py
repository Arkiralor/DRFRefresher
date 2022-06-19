
class UnitCoverter:
    """
    Class to hold methods to convert units from one to another.

    Primarily to convert outdated, inefficient imperial units
    to standardised metric units.
    """

    KM_TO_MILE = 1.6

    @classmethod
    def mile_to_km(cls, kilometres:float=1.00):
        return kilometres*cls.KM_TO_MILE

    @classmethod
    def faranheit_to_celcius(cls, deg_far: float=32.00):
        return (deg_far-32)/1.8000