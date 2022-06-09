# Generated by Django 4.0.4 on 2022-06-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationapp', '0002_countrymodel_country_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrymodel',
            name='country_region',
            field=models.CharField(blank=True, help_text='Region of the country.', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='countrymodel',
            name='name',
            field=models.CharField(help_text='Common name of the country.', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='countrymodel',
            name='official_name',
            field=models.CharField(blank=True, help_text='Official name of the country as presented in legal documents.', max_length=50, null=True),
        ),
    ]