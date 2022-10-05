from django.db import models
from django.template.defaultfilters import slugify

from payment_app.model_choices import SubscriptionTransactionChoice
from userapp.models import User

import uuid

# Create your models here.


class SubscriptionOrder(models.Model):
    """
    Model for a Subscription Order
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    payment_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    order_description = models.TextField()
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    currency = models.CharField(
        max_length=10,
        default='INR'
    )
    is_paid = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.order_description}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.uuid)
        super(SubscriptionOrder, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Subscription Order"
        verbose_name_plural = "Subscription Orders"
        ordering = ('-created_at',)
        unique_together = ('user', 'order_description', 'created_at')


class SubscriptionTransaction(models.Model):
    """
    Model for a Subscription Transaction
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    subscription_order = models.ForeignKey(
        SubscriptionOrder,
        on_delete=models.CASCADE
    )
    transaction_id = models.CharField(
        max_length=128
    )
    transaction_amount = models.DecimalField(
        max_digits=16,
        decimal_places=2
    )
    transaction_status = models.CharField(
        max_length=128,
        choices=SubscriptionTransactionChoice.STATUS_CHOICE,
        default=SubscriptionTransactionChoice.pending
    )
    transaction_timestamp = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.subscription_order.user.username} - {self.transaction_id}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.uuid)
        super(SubscriptionTransaction, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Subscription Transaction"
        verbose_name_plural = "Subscription Transactions"


class UpcomingSubscription(models.Model):
    """
    Model for a Upcoming Subscription
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        SubscriptionOrder,
        on_delete=models.CASCADE,
        related_name='order'
    )
    transaction = models.ForeignKey(
        SubscriptionTransaction,
        on_delete=models.CASCADE
    )
    start_on = models.DateTimeField(
        null=True,
        blank=True
    )
    end_on = models.DateTimeField(
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.user.username} - {self.order.order_description}"

    class Meta:
        verbose_name = "Upcoming Subscription"
        verbose_name_plural = "Upcoming Subscriptions"


class Subscriber(models.Model):
    """
    Model for a Subscription
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        SubscriptionOrder,
        on_delete=models.CASCADE
    )
    is_subscribed = models.BooleanField(
        default=False
    )
    subscribed_from = models.DateTimeField(
        null=True,
        blank=True
    )
    subscribed_till = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.order.order_description}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(Subscriber, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers "
        ordering = ('-subscribed_from',)
        unique_together = ('user', 'order', 'subscribed_from')
