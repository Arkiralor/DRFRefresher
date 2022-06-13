from core import settings
from django.core.mail import send_mail
from typing import List
from userapp import logger


class EmailHelper:

    sender = settings.EMAIL_HOST_USER

    @classmethod
    def send_new_user_email(cls, user, recipients: List[str]):
        """
        Send an email to the recipient
        """
        recipient_list = []
        if len(recipients) < 1:
            raise Exception("No recipients provided")

        for recipient in recipients:
            recipient_list.append(str(recipient))

        subject = f"New User: {user.username} Registered"
        message = f"A new user has registered: {user.username} via the userapp.add API."

        try:
            resp = send_mail(
                    subject=subject,
                    message=message,
                    from_email=cls.sender,
                    recipient_list=recipient_list
                )
            logger.info(f"Email Response: {resp}")
        except Exception as ex:
            logger.warn(f"Error sending email: {ex}")

if __name__ == "__main__":
    pass
