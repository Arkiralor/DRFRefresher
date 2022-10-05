import uuid

from django.db import models
from django.template.defaultfilters import slugify

from storyapp.model_choices import StoryChoice
from userapp.models import User


# Create your models here.

class Story(models.Model):
    """
    Model to hold individual stories.
    """
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=250, help_text="Title of the story.")
    story_banner = models.ImageField(
        upload_to='images/story_banners/',
        blank=True,
        default='images/defaults/story_banner.png',
        help_text="Banner image for the story (Ref: 1280x640px)."
    )
    slug = models.SlugField(max_length=250, null=True, blank=True)
    description = models.TextField(
        max_length=1000, null=True, blank=True, help_text="Short summary of the story.")
    body = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='story_author'
    )
    genre = models.CharField(
        max_length=32,
        choices=StoryChoice.GENRE_CHOICE,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        '''
        Extended save() method to create a slug for the story.
        '''
        self.slug = slugify(f"{self.title}-{self.author.username}")
        super(Story, self).save(*args, **kwargs)

    def __str__(self):
        rep = f"{self.title} by {self.author.username}"
        return rep

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
        ordering = ('-created_at',)
        unique_together = ('title', 'author')
