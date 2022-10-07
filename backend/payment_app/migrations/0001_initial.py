# Generated by Django 4.0.4 on 2022-07-31 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('payment_id', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('order_description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(default='INR', max_length=10)),
                ('is_paid', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Subscription Order',
                'verbose_name_plural': 'Subscription Orders',
                'ordering': ('-created_at',),
                'unique_together': {('user', 'order_description', 'created_at')},
            },
        ),
        migrations.CreateModel(
            name='SubscriptionTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('transaction_id', models.CharField(max_length=128)),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=16)),
                ('transaction_status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('failed', 'Failed'), ('refunded', 'Refunded'), ('reversal', 'Reversal')], default='pending', max_length=128)),
                ('transaction_timestamp', models.DateTimeField(blank=True, null=True)),
                ('subscription_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment_app.subscriptionorder')),
            ],
            options={
                'verbose_name': 'Subscription Transaction',
                'verbose_name_plural': 'Subscription Transactions',
            },
        ),
        migrations.CreateModel(
            name='UpcomingSubscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('start_on', models.DateTimeField(blank=True, null=True)),
                ('end_on', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='payment_app.subscriptionorder')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment_app.subscriptiontransaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Upcoming Subscription',
                'verbose_name_plural': 'Upcoming Subscriptions',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('is_subscribed', models.BooleanField(default=False)),
                ('subscribed_from', models.DateTimeField(blank=True, null=True)),
                ('subscribed_till', models.DateTimeField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment_app.subscriptionorder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers ',
                'ordering': ('-subscribed_from',),
                'unique_together': {('user', 'order', 'subscribed_from')},
            },
        ),
    ]