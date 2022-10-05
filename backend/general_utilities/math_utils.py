
class UnitCoverter:
    """
    Class to hold methods to convert units from one to another.

    Primarily to convert outdated, inefficient imperial units
    to standardised metric units.
    """

    KM_TO_MILE = 1.609
    FT_TO_METRE = 3.28084
    YARD_TO_METRE = 0.9144


    @classmethod
    def mile_to_km(cls, miles:float=0.621371):
        return miles*cls.KM_TO_MILE

    @classmethod
    def ft_to_metre(cls, feet:float=3.28084):
        return feet/cls.FT_TO_METRE

    @classmethod
    def yard_to_metre(cls, yards:float=0.9144):
        return yards*cls.YARD_TO_METRE

    @classmethod
    def faranheit_to_celcius(cls, deg_far: float=32.00):
        return (deg_far-32)/1.8000