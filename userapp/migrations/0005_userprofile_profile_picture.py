# Generated by Django 4.0.4 on 2022-06-19 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_user_blocked_until_user_unsuccessful_login_attempts'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/defaults/profile_picture.png', upload_to='images/profile_pictures/'),
        ),
    ]
