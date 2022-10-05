from datetime import timedelta
import uuid

from django.core.validators import EmailValidator, RegexValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from constants.reference_values import StringConstant
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
    unsuccessful_login_attempts = models.PositiveIntegerField(
        default=0,
        blank=True,
        null=True,
        help_text="Number of unsuccessful login attempts"
    )
    blocked_until = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Blocked until"
    )


    def save(self, *args, **kwargs):
        '''
        Extended save() method to create a slug for the user.
        '''
        self.username = self.username.lower()
        self.email = self.email.lower()
        ## prithoo: Create a slug, every time the user is updated.
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
    profile_slug = models.SlugField(max_length=250, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='images/profile_pictures/',
        blank=True,
        default='images/defaults/profile_picture.png'
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

    def save(self, *args, **kwargs):
        '''
        Extended save() method to create a slug for the user.
        '''
        ## prithoo: Create a slug, every time the user is updated.
        self.profile_slug = slugify(
            f"profile{StringConstant.hypen}{self.user.user_slug}")
        super(UserProfile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        ordering = ('-created_at', 'id')


class UserOTP(models.Model):
    """
    Model to hold one-time-passwords generated for users to login with.
    """
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assigned_user'
    )
    otp = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        """
        Extended save() method to auto-generate an exipration for the OTP.
        """
        self.expiry = timezone.now() + timedelta(minutes=15)
        super(UserOTP, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'User OTP'
        verbose_name_plural = 'User OTPs'
        ordering = ('-created_at', 'id')
