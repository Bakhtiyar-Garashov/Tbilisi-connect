# Generated by Django 3.2.5 on 2021-08-06 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_auto_20210801_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='WelcomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Welcome page title')),
                ('subtitle_en', models.TextField(verbose_name='Welcome page text (en)')),
                ('subtitle_ge', models.TextField(verbose_name='Welcome page text (ge)')),
                ('subtitle_ru', models.TextField(verbose_name='Welcome page text (ru)')),
                ('image', models.ImageField(upload_to='images', verbose_name='Image')),
                ('url_main', models.URLField(blank=True, null=True, verbose_name='Main url (e.g., website url)')),
                ('url_facebook', models.URLField(blank=True, null=True, verbose_name='Facebook page')),
                ('url_instagram', models.URLField(blank=True, null=True, verbose_name='Instagram page')),
                ('url_twitter', models.URLField(blank=True, null=True, verbose_name='Twitter account')),
            ],
            options={
                'verbose_name': 'Welcome page configuration',
                'verbose_name_plural': 'Welcome page configurations',
            },
        ),
    ]
