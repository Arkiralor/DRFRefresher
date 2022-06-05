"""
This module stores the signals used in the storyapp.
"""
from django.db.models.signals import post_save, post_delete, m2m_changed

from storyapp.models import Story


class StorySignalReciever:
    """
    Class to store all signals used in the storyapp.
    """
    model = Story

    @classmethod
    def story_created(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a story is created.
        """
        if created:
            print(f"Story: {instance.title} created \nby Author: {instance.author.username}.")

    @classmethod
    def story_updated(cls, sender, instance, created, **kwargs):
        """
        Signal to send when a story is updated.
        """
        if not created:
            print(f"Story {instance.title} updated \nby User {instance.author.username}.")

    @classmethod
    def story_deleted(cls, sender, instance, **kwargs):
        """
        Signal to send when a story is deleted.
        """
        print(f"Story {instance.title} deleted \nby User {instance.author.username}.")

post_save.connect(receiver=StorySignalReciever.story_created, sender=StorySignalReciever.model)
post_save.connect(receiver=StorySignalReciever.story_updated, sender=StorySignalReciever.model)
post_delete.connect(receiver=StorySignalReciever.story_deleted, sender=StorySignalReciever.model)
