from django.apps import AppConfig


class StoryappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'storyapp'

    def ready(self):
        import userapp.signals
