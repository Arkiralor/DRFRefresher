from django.db.models.signals import post_save, post_delete

from blacklist import logger
from blacklist.models import BlacklistedEmail, BlacklistedPhoneNumber, BlacklistedPassword


class BlacklistedEmailSignal(object):
    """
    Signal to handle the creation and deletion of BlacklistedEmail models.
    """
    model = BlacklistedEmail

    @classmethod
    def email_blacklisted(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a BlacklistedEmail is created.
        """
        if created:
            logger.info(f"BlacklistedEmail: {instance.email} created.")

    @classmethod
    def email_unblacklisted(cls, sender, instance, **kwargs):
        """
        Signal to send when a BlacklistedEmail is deleted.
        """
        logger.info(f"BlacklistedEmail: {instance.email} deleted.")


post_save.connect(receiver=BlacklistedEmailSignal.email_blacklisted,
                  sender=BlacklistedEmailSignal.model)
post_delete.connect(receiver=BlacklistedEmailSignal.email_unblacklisted,
                    sender=BlacklistedEmailSignal.model)


class BlacklistedPhoneNumberSignal(object):

    model = BlacklistedPhoneNumber

    @classmethod
    def phone_blacklisted(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a BlacklistedPhoneNumber is created.
        """
        if created:
            logger.info(
                f"BlacklistedPhoneNumber: {instance.phone_number} created.")

    @classmethod
    def phone_unblacklisted(cls, sender, instance, **kwargs):
        """
        Signal to send when a BlacklistedPhoneNumber is deleted.
        """
        logger.info(
            f"BlacklistedPhoneNumber: {instance.phone_number} deleted.")


post_save.connect(receiver=BlacklistedPhoneNumberSignal.phone_blacklisted,
                  sender=BlacklistedPhoneNumberSignal.model)
post_delete.connect(receiver=BlacklistedPhoneNumberSignal.phone_unblacklisted,
                    sender=BlacklistedPhoneNumberSignal.model)


class BlacklistedPasswordSignal(object):

    model = BlacklistedPassword

    @classmethod
    def password_blacklisted(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a BlacklistedPassword is created.
        """
        if created:
            logger.info(f"BlacklistedPassword: {instance.password} created.")

    @classmethod
    def password_unblacklisted(cls, sender, instance, **kwargs):
        """
        Signal to send when a BlacklistedPassword is deleted.
        """
        logger.info(f"BlacklistedPassword: {instance.password} deleted.")


post_save.connect(receiver=BlacklistedPasswordSignal.password_blacklisted,
                  sender=BlacklistedPasswordSignal.model)
post_delete.connect(receiver=BlacklistedPasswordSignal.password_unblacklisted,
                    sender=BlacklistedPasswordSignal.model)


if __name__ == "__main__":
    pass
