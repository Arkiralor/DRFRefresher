from datetime import datetime
import uuid

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from userapp.model_choices import USER_TYPE_CHOICES

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
    email = models.EmailField(unique=True)
    user_slug = models.SlugField(max_length=250, null=True, blank=True)
    user_type = models.CharField(
        max_length=32,
        choices=USER_TYPE_CHOICES,
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
        ordering = ('-id', '-date_joined')
