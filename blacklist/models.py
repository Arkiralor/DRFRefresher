from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator, RegexValidator

from userapp.constants import UserRegex
import uuid

# Create your models here.

class BlacklistedPassword(models.Model):
    """
    Model to store passwords that are blacklisted.
    """
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    plaintext_password = models.CharField(max_length=128, unique=True)
    hashed_value = models.CharField(max_length=256, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Override the save method to hash the password.
        """
        self.hashed_value = make_password(self.plaintext_password)

        super(BlacklistedPassword, self).save(*args, **kwargs)

    def __str__(self):
        return self.plaintext_password
        

    class Meta:
        verbose_name = "Blacklisted Password"
        verbose_name_plural = "Blacklisted Passwords"
        unique_together = ('plaintext_password', 'hashed_value')
        ordering = ('-date_added',)


class BlacklistedEmail(models.Model):
    """
    Model to store emails that are blacklisted.
    """
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    email = models.EmailField(
            unique=True, 
            validators=[
                EmailValidator(
                    message="Please enter a valid email address.",
                    code="invalid_email"
                )
            ]
        )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        """
        Override the save method to normalize the email ID.
        """
        self.email = self.email.lower()
        super(BlacklistedEmail, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Blacklisted Email"
        verbose_name_plural = "Blacklisted Emails"
        ordering = ('-date_added',)


class BlacklistedPhoneNumber(models.Model):
    """
    Model to store phone numbers that are blacklisted.
    """
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    phone_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=UserRegex.PHONE_REGEX_IN,
                message="Please enter a valid phone number.",
                code="invalid_phone"
            )
        ],
        unique=True
    )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "Blacklisted Phone Number"
        verbose_name_plural = "Blacklisted Phone Numbers"
        ordering = ('-date_added',)

