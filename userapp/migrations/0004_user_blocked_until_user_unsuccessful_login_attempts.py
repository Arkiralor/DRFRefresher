# Generated by Django 4.0.4 on 2022-06-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_alter_userotp_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='blocked_until',
            field=models.DateTimeField(blank=True, help_text='Blocked until', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='unsuccessful_login_attempts',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Number of unsuccessful login attempts', null=True),
        ),
    ]
