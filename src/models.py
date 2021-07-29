from django.contrib.gis.db import models

# Create your models here.

class Objects(models.Model):
    name = models.CharField(max_length=50)
    description_en = models.TextField(blank=True,null=True)
    description_ge = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    location = models.PointField(srid=4326)

    class Meta:
        ordering=['name']
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'


    def __str__(self) -> str:
        return f"{self.name}"