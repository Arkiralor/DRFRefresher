from rest_framework import serializers
from userapp.models import User
# Define your serializers here:


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    class Meta:
        model = User
        fields = '__all__'


class UserAdminSerializer(serializers.ModelSerializer):
    """
    Serializer for User model when an admin is viewing.
    """
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'read_only': True
            }
        }
