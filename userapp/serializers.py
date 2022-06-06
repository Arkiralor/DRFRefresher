from rest_framework import serializers
from userapp.models import User

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
        fields = (
            'id',
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'user_phone_primary',
            'user_slug',
            'user_type',
            'last_login', 
            'is_superuser', 
            'is_staff', 
            'is_active', 
            'date_joined'
        )
        extra_kwargs = {
            'password': {
                'read_only': True
            }
        }
