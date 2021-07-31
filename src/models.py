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
    tags = models.ManyToManyField(Tag,related_name='tags')
    url_main = models.URLField(null=True, blank=True, verbose_name='Main url (e.g., website url)')
    url_facebook = models.URLField(null=True, blank=True, verbose_name='Facebook page')
    url_instagram = models.URLField(null=True, blank=True, verbose_name='Instagram page')
    url_twitter = models.URLField(null=True, blank=True, verbose_name='Twitter account')
    description_en = models.TextField(blank=True, null=True, verbose_name='Description (EN)')
    description_ge = models.TextField(blank=True, null=True, verbose_name='Description (GE)')
    description_ru = models.TextField(blank=True, null=True, verbose_name='Description (RU)')
    location = models.PointField(srid=4326,verbose_name='Location on map')

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self) -> str:
        return f"{self.name}"
