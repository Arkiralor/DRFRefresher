import secrets
from django.shortcuts import render
from core import settings
from django.core.mail import send_mail
from django.template.defaultfilters import slugify
from typing import List
from userapp import logger
from userapp.models import User, UserOTP

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import datetime
from os import environ
from secrets import token_hex


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
        body = render_to_string(
            template_name='email_templates/new_user.html', context=context)
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

    @classmethod
    def send_otp_email(cls, user, otp: str, recipients: List[str]):
        """
        Send an email to the recipient
        """
        recipient_list = []
        if len(recipients) < 1:
            raise Exception("No recipients provided")

        for recipient in recipients:
            recipient_list.append(str(recipient))

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
            logger.info(f"Email sent to {recipient_list}: {resp}")
        except Exception as ex:
            logger.warn(f"Error sending email: {ex}")


class OTPHelper:

    @classmethod
    def generate_otp(cls):
        """
        Generate a random OTP
        """
        logger.info("Generating OTP")
        part_1 = token_hex(2)
        part_2 = token_hex(2)

        otp = slugify(f"{part_1}-{part_2}")
        return otp


if __name__ == "__main__":
    pass
