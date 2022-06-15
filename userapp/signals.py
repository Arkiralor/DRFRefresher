"""
This module stores the signals used in the storyapp.
"""
from django.db.models.signals import post_save, post_delete, m2m_changed
from os import environ

from userapp.models import User, UserProfile, UserOTP
from userapp.helpers import EmailHelper
from userapp import logger


class UserSignalReciever:
    """
    Class to store all signals used in the storyapp.
    """
    model = User
    notification_reciever = environ.get("MANAGER_EMAIL", "")

    @classmethod
    def user_created(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a story is created.
        """
        if created:
            logger.info(f"User: {instance.username} created.")
            # Create a profile for the user upon creation.
            profile = UserProfile.objects.create(user=instance)
            profile.save()
            ## TODO: Implement an email notification queue to the user.
            ## otherwise, this process takes too long.
            EmailHelper.send_new_user_email(
                    user=instance, 
                    recipients=[
                        cls.notification_reciever
                    ]
                )

    @classmethod
    def user_updated(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a story is updated.
        """
        if not created:
            logger.info(f"User {instance.username} updated.")
            profile = UserProfile.objects.get(user=instance)
            profile.save()

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


class UserProfileSignalReciever:
    """
    Class to store all signals used in the storyapp.
    """
    model = UserProfile

    @classmethod
    def userprofile_created(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a story is created.
        """
        if created:
            logger.info(
                f"UserProfile: {instance.id} created for User: {instance.user.username}.")
            

    @classmethod
    def userprofile_updated(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a story is updated.
        """
        if not created:
            logger.info(
                f"UserProfile: {instance.id} updated for User: {instance.user.username}.")

    @classmethod
    def userprofile_deleted(cls, sender, instance, **kwargs):
        """
        Signal to send when a story is deleted.
        """
        logger.info(
            f"UserProfile: {instance.id} deleted for User: {instance.user.username}.")


## Signal to send when a userprofile is created.
post_save.connect(receiver=UserProfileSignalReciever.userprofile_created,
                  sender=UserProfileSignalReciever.model)
## Signal to send when a userprofile is updated.
post_save.connect(receiver=UserProfileSignalReciever.userprofile_updated,
                  sender=UserProfileSignalReciever.model)
## Signal to send when a userprofile is deleted.
post_delete.connect(receiver=UserProfileSignalReciever.userprofile_deleted,
                    sender=UserProfileSignalReciever.model)



class UserOTPSignalReciever:
    """
    Class to store all signals used in the storyapp.
    """
    model = UserOTP

    @classmethod
    def userotp_created(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a story is created.
        """
        if created:
            logger.info(
                f"UserOTP: {instance.id} created for User: {instance.user.username}.")
        
    @classmethod
    def userotp_updated(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a story is updated.
        """
        if not created:
            logger.info(
                f"UserOTP: {instance.id} updated for User: {instance.user.username}.")

    @classmethod
    def userotp_deleted(cls, sender, instance, **kwargs):
        """
        Signal to send when a story is deleted.
        """
        logger.info(
            f"UserOTP: {instance.id} deleted for User: {instance.user.username}.")


## Signal to send when a userotp is created.
post_save.connect(receiver=UserOTPSignalReciever.userotp_created,
                    sender=UserOTPSignalReciever.model)
## Signal to send when a userotp is updated.
post_save.connect(receiver=UserOTPSignalReciever.userotp_updated,
                    sender=UserOTPSignalReciever.model)
## Signal to send when a userotp is deleted.
post_delete.connect(receiver=UserOTPSignalReciever.userotp_deleted,
                    sender=UserOTPSignalReciever.model)
                    