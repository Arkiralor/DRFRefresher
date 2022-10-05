from rest_framework import serializers
from payment_app.models import SubscriptionOrder, SubscriptionTransaction, UpcomingSubscription, Subscriber
from userapp.serializers import UserSearchSerializer


class SubscriptionOrderSerializer(serializers.ModelSerializer):
    """
    Serializer for SubscriptionOrder model.
    """
    user = UserSearchSerializer(read_only=True)

    class Meta:
        model = SubscriptionOrder
        fields = '__all__'


class SubscriptionTransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for SubscriptionTransaction model.
    """
    subscription_order = SubscriptionOrderSerializer()

    class Meta:
        model = SubscriptionTransaction
        fields = '__all__'


class UpcomingSubscriptionSerializer(serializers.ModelSerializer):
    """
    Serializer for UpcomingSubscription model.
    """
    user = UserSearchSerializer(read_only=True)
    transaction = SubscriptionTransactionSerializer()

    class Meta:
        model = UpcomingSubscription
        fields = '__all__'


class SubscriberSerializer(serializers.ModelSerializer):
    """
    Serializer for Subscriber model.
    """
    user = UserSearchSerializer(read_only=True)
    order = SubscriptionOrderSerializer()

    class Meta:
        model = Subscriber
        fields = '__all__'
