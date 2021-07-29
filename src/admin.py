from django.contrib import admin
from .models import Objects
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class ObjectsAdmin(LeafletGeoAdmin, admin.ModelAdmin):
    list_display=('name',)
    ordering =('name',)
    list_filter=('name',)
    search_fields=('name',)

admin.site.register(Objects,ObjectsAdmin)
