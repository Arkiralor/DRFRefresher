import uuid

from django.template.defaultfilters import slugify


class ModelUtils:
    """
    Utility class for user models.
    """
    @classmethod
    def create_slug(cls, model_instance, field_name):
        """
        Create a unique slug for a model instance.
        """
        slug = getattr(model_instance, field_name)
        slug = slugify(str(slug))
        return slug

    @classmethod
    def create_uuid(cls):
        """
        Create a unique uuid.
        """
        return uuid.uuid4()
