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
    def blacklisted_email_updated(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a BlacklistedEmail is updated.
        """
        if not created:
            logger.info(f"BlacklistedEmail: {instance.email} updated.")

    @classmethod
    def email_unblacklisted(cls, sender, instance, **kwargs):
        """
        Signal to send when a BlacklistedEmail is deleted.
        """
        logger.info(f"BlacklistedEmail: {instance.email} deleted.")


post_save.connect(receiver=BlacklistedEmailSignal.email_blacklisted,
                  sender=BlacklistedEmailSignal.model)
post_save.connect(receiver=BlacklistedEmailSignal.blacklisted_email_updated,
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
                f"Blacklisted Phone Number: {instance.phone_number} created.")

    @classmethod
    def blacklisted_phone_number_updated(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a BlacklistedPhoneNumber is updated.
        """
        if not created:
            logger.info(
                f"Blacklisted Phone Number: {instance.phone_number} updated.")

    @classmethod
    def phone_unblacklisted(cls, sender, instance, **kwargs):
        """
        Signal to send when a BlacklistedPhoneNumber is deleted.
        """
        logger.info(
            f"Blacklisted Phone Number: {instance.phone_number} deleted.")


post_save.connect(receiver=BlacklistedPhoneNumberSignal.phone_blacklisted,
                  sender=BlacklistedPhoneNumberSignal.model)
post_save.connect(receiver=BlacklistedPhoneNumberSignal.blacklisted_phone_number_updated,
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
            logger.info(f"Blacklisted Password: {instance.plaintext_password} created.")

    @classmethod
    def blacklisted_password_updated(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a BlacklistedPassword is updated.
        """
        if not created:
            logger.info(f"Blacklisted Password: {instance.plaintext_password} updated.")

    @classmethod
    def password_unblacklisted(cls, sender, instance, **kwargs):
        """
        Signal to send when a BlacklistedPassword is deleted.
        """
        logger.info(f"Blacklisted Password: {instance.plaintext_password} deleted.")


post_save.connect(receiver=BlacklistedPasswordSignal.password_blacklisted,
                  sender=BlacklistedPasswordSignal.model)
post_save.connect(receiver=BlacklistedPasswordSignal.blacklisted_password_updated,
                  sender=BlacklistedPasswordSignal.model)
post_delete.connect(receiver=BlacklistedPasswordSignal.password_unblacklisted,
                    sender=BlacklistedPasswordSignal.model)


if __name__ == "__main__":
    pass
