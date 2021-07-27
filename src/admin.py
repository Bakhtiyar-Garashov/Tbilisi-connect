from django.contrib import admin
from .models import Objects
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
admin.site.register(Objects, LeafletGeoAdmin)