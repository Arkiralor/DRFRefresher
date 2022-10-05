from rest_framework import serializers

from blacklist.models import BlacklistedEmail, BlacklistedPhoneNumber, BlacklistedPassword


class BlacklistedEmailSerializer(serializers.ModelSerializer):
    """
    Serializer for BlacklistedEmail model.
    """
    class Meta:
        model = BlacklistedEmail
        fields = ('id', 'email', 'date_added')


class BlacklistedPhoneNumberSerializer(serializers.ModelSerializer):
    """
    Serializer for BlacklistedPhoneNumber model.
    """
    class Meta:
        model = BlacklistedPhoneNumber
        fields = ('id', 'phone_number', 'date_added')


class BlacklistedPasswordSerializer(serializers.ModelSerializer):
    """
    Serializer for BlacklistedPassword model.
    """
    class Meta:
        model = BlacklistedPassword
        fields = ('id', 'plaintext_password', 'date_added')

