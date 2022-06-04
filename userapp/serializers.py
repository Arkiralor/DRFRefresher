from rest_framework import serializers
from .models import User
# Define your serializers here:


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_type')
        read_only_fields = ('id',)
        extra_kwargs = {
            'username': {
                'required': True,
                'min_length': 5,
                'max_length': 32,
                'error_messages': {
                    'required': 'Username is required.',
                    'min_length': 'Username must be at least 5 characters long.',
                    'max_length': 'Username must be at most 32 characters long.'
                }
            },
            'email': {
                'required': True,
                'error_messages': {
                    'required': 'Email is required.'
                }
            }
        }


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
