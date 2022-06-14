from django.shortcuts import render
from core import settings
from django.core.mail import send_mail
from typing import List
from userapp import logger

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import datetime
from os import environ


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
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        site = environ.get('APP_NAME', '')
        context = {
            "user": user.username,
            "timestamp": timestamp,
            "site": site
        }
        body = render_to_string(template_name='email_templates/new_user.html', context=context)
        email = EmailMessage(
                subject=subject, 
                body=body, 
                to=recipient_list
            )
        try:
            resp = email.send()
            logger.info(f"Email sent to {recipient_list}: {resp}")
        except Exception as ex:
            logger.warn(f"Error sending email: {ex}")


if __name__ == "__main__":
    pass
