# Generated by Django 3.2.5 on 2021-08-01 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_auto_20210801_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='crypto_payment_option',
            field=models.BooleanField(default=False, verbose_name='Is cryptocurrency payment option available?'),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='url_google_map',
            field=models.URLField(blank=True, null=True, verbose_name='Google Maps location URL'),
        ),
    ]
