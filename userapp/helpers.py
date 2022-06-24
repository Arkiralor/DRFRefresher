from datetime import datetime
from os import environ
from secrets import token_hex, choice
from typing import List

from django.template.defaultfilters import slugify
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from core import settings
from userapp import logger


class EmailHelper:

    sender = settings.EMAIL_HOST_USER

    @classmethod
    def send_new_user_email(cls, user, recipients: List[str]):
        """
        Send an email to the recipient
        args:
            user: User model instance
            recipients: List[Plaintext email IDs]
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
        body = render_to_string(
            template_name='email_templates/new_user.html', context=context)
        email = EmailMessage(
            subject=subject,
            body=body,
            to=recipient_list
        )
        try:
            resp = email.send()
            logger.info(f"Email sent to {recipient_list[0]}: {resp}")
        except Exception as ex:
            logger.warn(f"Error sending email: {ex}")

    @classmethod
    def send_otp_email(cls, user, otp: str):
        """
        Send an email with the OTP to the user
        args:
            user: User model instance
            otp: Plaintext OTP
        """

        recipient_list = [user.email]

        subject = f"OTP for {user.username} Login"
        site = environ.get('APP_NAME', '')
        context = {
            "user": user.username,
            "otp": otp,
            "site": site
        }
        body = render_to_string(
            template_name='email_templates/otp_login.html', context=context)
        email = EmailMessage(
            subject=subject,
            body=body,
            to=recipient_list
        )
        try:
            resp = email.send()
            logger.info(f"Email sent to {recipient_list[0]}: {resp}")
        except Exception as ex:
            logger.warn(f"Error sending email: {ex}")


class OTPHelper:

    num_list = [str(i) for i in range(1000, 10000)]

    @classmethod
    def generate_hex_otp(cls):
        """
        Generate a random OTP
        """
        logger.info("Generating OTP")

        ## OTP is a 4 character hex sequence
        part_1 = token_hex(2)
        part_2 = token_hex(2)

        otp = slugify(f"{part_1}-{part_2}")
        return otp

    @classmethod
    def generate_int_otp(cls):
        """
        Generate a random OTP
        """
        logger.info("Generating OTP")
        part_1 = choice(cls.num_list)
        part_2 = choice(cls.num_list)

        otp = slugify(f"{part_1}-{part_2}")
        return otp


if __name__ == "__main__":
    pass
