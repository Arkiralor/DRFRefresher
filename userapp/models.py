from datetime import datetime
import uuid

from django.core.validators import EmailValidator, RegexValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from locationapp.models import LocationModel
from userapp.model_choices import UserChoice
from userapp.constants import UserRegex
# Create your models here.


class User(AbstractUser):
    """
    Model to store site-user information.
    """
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    email = models.EmailField(
        validators=[
            EmailValidator(
                message="Please enter a valid email address.",
                code="invalid_email"
            )
        ],
        unique=True
    )
    user_phone_primary = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=UserRegex.PHONE_REGEX_IN,
                message="Please enter a valid phone number.",
                code="invalid_phone"
            )
        ],
        blank=True,
        null=True
    )
    user_slug = models.SlugField(max_length=250, null=True, blank=True)
    user_type = models.CharField(
        max_length=32,
        choices=UserChoice.TYPE_CHOICES,
        default='normal_user',
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        '''
        Extended save() method to create a slug for the user.
        '''
        if not self.id or not self.user_slug:
            self.user_slug = slugify(f"{self.username}-{self.email}")
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('-date_joined', 'id')


class UserProfile(models.Model):
    """
    Model to store user profile information.
    """
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='owning_user'
    )
    headline = models.CharField(max_length=128, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.ForeignKey(
        LocationModel,
        on_delete=models.SET_NULL,
        related_name='user_location',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        ordering = ('-created_at', 'id')
