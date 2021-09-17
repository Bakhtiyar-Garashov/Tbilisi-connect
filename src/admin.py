from django.contrib import admin
from .models import Restaurants, Tag, WelcomePage
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class RestaurantsAdmin(LeafletGeoAdmin, admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.site_header = 'BazaraNet'
admin.site.index_title = 'BazaraNet adminstration'
admin.site.site_title = 'BazaraNet adminstration'
admin.site.register(Restaurants, RestaurantsAdmin)
admin.site.register(Tag)
admin.site.register(WelcomePage)