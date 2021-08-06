from django.contrib.gis.db import models

# Create your models here.


class Tag(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.text


class Restaurants(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    address = models.CharField(max_length=255, verbose_name='Address')
    image = models.ImageField(upload_to='images', verbose_name='Image')
    tags = models.ManyToManyField(Tag, related_name='tags')
    crypto_payment_option = models.BooleanField(
        default=False, verbose_name='Is cryptocurrency payment option available?')
    url_main = models.URLField(
        null=True, blank=True, verbose_name='Main url (e.g., website url)')
    url_facebook = models.URLField(
        null=True, blank=True, verbose_name='Facebook page')
    url_instagram = models.URLField(
        null=True, blank=True, verbose_name='Instagram page')
    url_twitter = models.URLField(
        null=True, blank=True, verbose_name='Twitter account')
    url_google_map = models.URLField(
        null=True, blank=True, verbose_name='Google Maps location URL')
    description_en = models.TextField(
        blank=True, null=True, verbose_name='Description (EN)')
    description_ge = models.TextField(
        blank=True, null=True, verbose_name='Description (GE)')
    description_ru = models.TextField(
        blank=True, null=True, verbose_name='Description (RU)')
    location = models.PointField(srid=4326, verbose_name='Location on map')

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self) -> str:
        return f"{self.name}"


class WelcomePage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Welcome page title')
    subtitle_en = models.TextField(verbose_name='Welcome page text (en)')
    subtitle_ge = models.TextField(verbose_name='Welcome page text (ge)')
    subtitle_ru = models.TextField(verbose_name='Welcome page text (ru)')
    image = models.ImageField(upload_to='images', verbose_name='Image')
    url_main = models.URLField(
        null=True, blank=True, verbose_name='Main url (e.g., website url)')
    url_facebook = models.URLField(
        null=True, blank=True, verbose_name='Facebook page')
    url_instagram = models.URLField(
        null=True, blank=True, verbose_name='Instagram page')
    url_twitter = models.URLField(
        null=True, blank=True, verbose_name='Twitter account')

    class Meta:
        verbose_name = 'Welcome page configuration'
        verbose_name_plural = 'Welcome page configurations'

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if WelcomePage.objects.exists():
            raise ValueError("Please modify existing text for Welcome page. Cannot add multiple one")
        else:
            super().save(*args, **kwargs)