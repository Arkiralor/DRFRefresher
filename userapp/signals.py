"""
This module stores the signals used in the storyapp.
"""
from django.db.models.signals import post_save, post_delete, m2m_changed

from userapp.models import User
from userapp import logger


class UserSignalReciever:
    """
    Class to store all signals used in the storyapp.
    """
    model = User

    @classmethod
    def user_created(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a story is created.
        """
        if created:
            logger.info(f"User: {instance.username} created.")

    @classmethod
    def user_updated(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a story is updated.
        """
        if not created:
            logger.info(f"User {instance.username} updated.")

    @classmethod
    def user_deleted(cls, sender, instance, **kwargs):
        """
        Signal to send when a story is deleted.
        """
        logger.info(f"User {instance.username} deleted.")

## Signal to send when a user is created.
post_save.connect(receiver=UserSignalReciever.user_created,
                  sender=UserSignalReciever.model)
## Signal to send when a user is updated.
post_save.connect(receiver=UserSignalReciever.user_updated,
                  sender=UserSignalReciever.model)
## Signal to send when a user is deleted.
post_delete.connect(receiver=UserSignalReciever.user_deleted,
                    sender=UserSignalReciever.model)
