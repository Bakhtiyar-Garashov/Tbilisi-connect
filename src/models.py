from django.contrib.gis.db import models

# Create your models here.

class Objects(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField(srid=4326)

    def __str__(self) -> str:
        return f"{self.name}'s location"