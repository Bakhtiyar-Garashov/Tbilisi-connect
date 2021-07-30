# Generated by Django 3.2.5 on 2021-07-30 19:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_auto_20210729_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images')),
                ('url_main', models.URLField(blank=True, null=True)),
                ('url_facebook', models.URLField(blank=True, null=True)),
                ('url_instagram', models.URLField(blank=True, null=True)),
                ('url_twitter', models.URLField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_ge', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name': 'Restaurant',
                'verbose_name_plural': 'Restaurants',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['text'],
            },
        ),
        migrations.DeleteModel(
            name='Objects',
        ),
        migrations.AddField(
            model_name='restaurants',
            name='tags',
            field=models.ManyToManyField(to='src.Tag'),
        ),
    ]
