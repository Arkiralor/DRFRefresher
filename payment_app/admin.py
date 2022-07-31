from django.contrib import admin
from payment_app.models import SubscriptionOrder, SubscriptionTransaction, UpcomingSubscription, Subscriber

# Register your models here.

@admin.register(SubscriptionOrder)
class SubscriptionOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_id', 'order_description',
                    'user', 'amount', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at', 'updated_at')
    search_fields = ('order_description', 'user__username')
    ordering = ('-created_at',)

@admin.register(SubscriptionTransaction)
class SubscriptionTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscription_order', 'transaction_id',
                    'transaction_amount','transaction_status')
    list_filter = ('subscription_order__user', 'transaction_status')
    search_fields = ('subscription_order__order_description',
                     'subscription_order__user__username')
    ordering = ('-subscription_order__created_at',)

@admin.register(UpcomingSubscription)
class UpcomingSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'transaction')
    list_filter = ('user',)
    search_fields = ('user__username',
                     'transaction__subscription_order__order_description')
    ordering = ('-transaction__subscription_order__created_at',)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order', 'subscribed_from', 'subscribed_till')
    list_filter = ('user', 'subscribed_from', 'subscribed_till')
    search_fields = ('user__username', 'order__order_description')
    ordering = ('-subscribed_from',)
