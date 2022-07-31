from django.contrib import admin
from payment_app.models import SubscriptionOrder, SubscriptionTransaction, UpcomingSubscription, Subscriber

# Register your models here.


class SubscriptionOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_id', 'order_description',
                    'user', 'amount', 'created_on', 'updated_on')
    list_filter = ('user', 'created_on', 'updated_on')
    search_fields = ('order_description', 'user__username')
    ordering = ('-created_on',)


class SubscriptionTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscription_order', 'transaction_id',
                    'amount', 'currency', 'is_paid', 'created_on', 'updated_on')
    list_filter = ('subscription_order__user', 'created_on', 'updated_on')
    search_fields = ('subscription_order__order_description',
                     'subscription_order__user__username')
    ordering = ('-created_on',)


class UpcomingSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'transaction', 'created_on', 'updated_on')
    list_filter = ('user', 'created_on', 'updated_on')
    search_fields = ('user__username',
                     'transaction__subscription_order__order_description')
    ordering = ('-created_on',)


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order', 'created_on', 'updated_on')
    list_filter = ('user', 'created_on', 'updated_on')
    search_fields = ('user__username', 'order__order_description')
    ordering = ('-created_on',)
