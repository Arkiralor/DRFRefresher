import razorpay
from secrets import token_hex, choice
from payment_app.models import SubscriptionOrder, SubscriptionTransaction, UpcomingSubscription, Subscriber
from payment_app.serializers import SubscriptionOrderSerializer, SubscriptionTransactionSerializer, UpcomingSubscriptionSerializer, SubscriberSerializer

from core import settings
from datetime import timedelta
from django.utils import timezone


class RazorpayPaymentHandler:
    razorpay_key = settings.RAZORPAY_KEY
    razorpay_secret = settings.RAZORPAY_SECRET

    @classmethod
    def create_sub_order(cls, user_id=None, amount: int = None, currency: str = None, order_description: str = None, *args, **kwargs):
        """
        Create an order for the amount
        args:
            amount: Amount in cents
            currency: Currency code
            order_description: Order description
        """
        order_data = {
            "amount": amount,
            "currency": currency/100,
            "receipt": order_description,
            "payment_capture": 1
        }
        client = razorpay.Client(auth=(cls.razorpay_key, cls.razorpay_secret))
        order = client.order.create(order_data)
        new_subscription_order = SubscriptionOrder.objects.create(
            user=user_id,
            payment_id=order.get('id'),
            order_description=order_description,
            amount=amount,
            currency=currency
        )

        return new_subscription_order

    @classmethod
    def handle_sub_order_payment(cls, order_id: str):
        """
        Handle the payment for the order
        args:
            order_id: Order ID
        """
        client = razorpay.Client(auth=(cls.razorpay_key, cls.razorpay_secret))
        order = client.order.fetch(order_id)
        if not order.get('status') == 'paid':
            new_subscription_transaction, _ = SubscriptionTransaction.objects.get_or_create(
                subscription_order=subscription_order,
                transaction_id=order.get('id'),
                transaction_amount=order.get('amount'),
                transaction_status=order.get('status')
            )
            resp = {
                "error": "Payment not successful for orderId: {}".format(order_id)
            }

        subscription_order = SubscriptionOrder.objects.get(payment_id=order_id)
        subscription_order.is_paid = True
        subscription_order.save()

        new_subscription_transaction, _ = SubscriptionTransaction.objects.get_or_create(
            subscription_order=subscription_order,
            transaction_id=order.get('id'),
            transaction_amount=order.get('amount'),
            transaction_status=order.get('status')
        )

        subscriber = Subscriber.objects.filter(
            user=subscription_order.user).first()
        if subscriber:
            upcoming_subscription = UpcomingSubscription.objects.create(
                user=subscription_order.user,
                start_on=subscriber.subscribed_till,
                end_on=subscriber.subscribed_till + timedelta(days=30),
            )

        subscriber.is_subscribed = True
        subscriber.subscribed_till = timezone.now()+timedelta(days=30)
        subscriber.order = subscription_order
        subscriber.save()

        order_serialized, transaction_serialized = SubscriptionOrderSerializer(
            subscription_order).data, SubscriptionTransactionSerializer(new_subscription_transaction).data
        resp = {
            "order": order_serialized,
            "transaction": transaction_serialized
        }

        return resp
