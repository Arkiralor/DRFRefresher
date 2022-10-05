from rest_framework.serializers import ModelSerializer
from storyapp.models import Story


class StorySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'  # '__all__' or list of fields
