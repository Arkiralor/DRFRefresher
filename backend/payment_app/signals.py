from django.db.models.signals import post_save, post_delete, m2m_changed
from os import environ
from payment_app.models import SubscriptionOrder, SubscriptionTransaction, UpcomingSubscription, Subscriber
from payment_app import logger


class SubscriptionOrderSignal:
    """
    Signal for SubscriptionOrder model.
    """
    model = SubscriptionOrder

    @classmethod
    def subscription_order_created(cls, sender, instance, created, **kwargs):
        """
        Post save signal for SubscriptionOrder model.
        """
        if created:
            logger.info(f"SubscriptionOrder: {instance.id} created.")

    @classmethod
    def subscription_order_updated(cls, sender, instance, created, **kwargs):
        """
        Post save signal for SubscriptionOrder model.
        """
        if not created:
            logger.info(f"SubscriptionOrder: {instance.id} updated.")

    @classmethod
    def subscription_order_deleted(cls, sender, instance, **kwargs):
        """
        Post delete signal for SubscriptionOrder model.
        """
        logger.info(f"SubscriptionOrder: {instance.id} deleted.")


post_save.connect(receiver=SubscriptionOrderSignal.subscription_order_created, sender=SubscriptionOrderSignal.model)
post_save.connect(receiver=SubscriptionOrderSignal.subscription_order_updated, sender=SubscriptionOrderSignal.model)
post_delete.connect(receiver=SubscriptionOrderSignal.subscription_order_deleted, sender=SubscriptionOrderSignal.model)


class SubscriptionTransactionSignal:
    """
    Signal for SubscriptionTransaction model.
    """
    model = SubscriptionTransaction

    @classmethod
    def subscription_transaction_created(cls, sender, instance, created, **kwargs):
        """
        Post save signal for SubscriptionTransaction model.
        """
        if created:
            logger.info(f"SubscriptionTransaction: {instance.id} created.")

    @classmethod
    def subscription_transaction_updated(cls, sender, instance, created, **kwargs):
        """
        Post save signal for SubscriptionTransaction model.
        """
        if not created:
            logger.info(f"SubscriptionTransaction: {instance.id} updated.")

    @classmethod
    def subscription_transaction_deleted(cls, sender, instance, **kwargs):
        """
        Post delete signal for SubscriptionTransaction model.
        """
        logger.info(f"SubscriptionTransaction: {instance.id} deleted.")


post_save.connect(receiver=SubscriptionTransactionSignal.subscription_transaction_created, sender=SubscriptionTransactionSignal.model)
post_save.connect(receiver=SubscriptionTransactionSignal.subscription_transaction_updated, sender=SubscriptionTransactionSignal.model)
post_delete.connect(receiver=SubscriptionTransactionSignal.subscription_transaction_deleted, sender=SubscriptionTransactionSignal.model)


class UpcomingSubscriptionSignal:
    """
    Signal for UpcomingSubscription model.
    """
    model = UpcomingSubscription

    @classmethod
    def upcoming_subscription_created(cls, sender, instance, created, **kwargs):
        """
        Post save signal for UpcomingSubscription model.
        """
        if created:
            logger.info(f"UpcomingSubscription: {instance.id} created.")

    @classmethod
    def upcoming_subscription_updated(cls, sender, instance, created, **kwargs):
        """
        Post save signal for UpcomingSubscription model.
        """
        if not created:
            logger.info(f"UpcomingSubscription: {instance.id} updated.")

    @classmethod
    def upcoming_subscription_deleted(cls, sender, instance, **kwargs):
        """
        Post delete signal for UpcomingSubscription model.
        """
        logger.info(f"UpcomingSubscription: {instance.id} deleted.")


post_save.connect(receiver=UpcomingSubscriptionSignal.upcoming_subscription_created, sender=UpcomingSubscriptionSignal.model)
post_save.connect(receiver=UpcomingSubscriptionSignal.upcoming_subscription_updated, sender=UpcomingSubscriptionSignal.model)
post_delete.connect(receiver=UpcomingSubscriptionSignal.upcoming_subscription_deleted, sender=UpcomingSubscriptionSignal.model)


class SubscriberSignal:
    """
    Signal for Subscriber model.
    """
    model = Subscriber

    @classmethod
    def subscriber_created(cls, sender, instance, created, **kwargs):
        """
        Post save signal for Subscriber model.
        """
        if created:
            logger.info(f"Subscriber: {instance.id} created.")

    @classmethod
    def subscriber_updated(cls, sender, instance, created, **kwargs):
        """
        Post save signal for Subscriber model.
        """
        if not created:
            logger.info(f"Subscriber: {instance.id} updated.")

    @classmethod
    def subscriber_deleted(cls, sender, instance, **kwargs):
        """
        Post delete signal for Subscriber model.
        """
        logger.info(f"Subscriber: {instance.id} deleted.")


post_save.connect(receiver=SubscriberSignal.subscriber_created, sender=SubscriberSignal.model)
post_save.connect(receiver=SubscriberSignal.subscriber_updated, sender=SubscriberSignal.model)
post_delete.connect(receiver=SubscriberSignal.subscriber_deleted, sender=SubscriberSignal.model)
        

    