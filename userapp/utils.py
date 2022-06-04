import uuid

class ModelUtils:
    """
    Utility class for models.
    """
    @staticmethod
    def create_slug(model_instance, field_name):
        """
        Create a unique slug for a model instance.
        """
        slug = getattr(model_instance, field_name)
        slug = slug.lower()
        return slug

    @staticmethod
    def create_uuid():
        """
        Create a unique uuid.
        """
        return uuid.uuid4()
