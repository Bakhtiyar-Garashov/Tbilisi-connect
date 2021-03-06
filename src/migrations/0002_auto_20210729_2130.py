# Generated by Django 3.2.5 on 2021-07-29 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objects',
            options={'ordering': ['name'], 'verbose_name': 'Restaurant', 'verbose_name_plural': 'Restaurants'},
        ),
        migrations.AddField(
            model_name='objects',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='objects',
            name='description_ge',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='objects',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
    ]
