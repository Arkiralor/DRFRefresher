import uuid

from django.template.defaultfilters import slugify
from typing import List


class ModelUtils:
    """
    Utility class for user models.
    """

    DEFAULT_ATTR: str = 'NaN'

    @classmethod
    def create_slug(cls, model_instance, field_names: List[str]) -> str:
        """
        Create a unique slug for a model instance.
        """
        field_list = []
        for name in field_names:
            field_list.append(getattr(model_instance, name, cls.DEFAULT_ATTR))
        slug = slugify('-'.join(field_list))
        return slug

    @classmethod
    def create_uuid(cls):
        """
        Create a unique uuid.
        """
        return uuid.uuid4()
