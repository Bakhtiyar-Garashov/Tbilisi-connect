from rest_framework_gis import serializers as geoserializers
from rest_framework import serializers
from .models import Restaurants, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('text',)


class RestaurantSerializer(geoserializers.GeoFeatureModelSerializer):
    """ Convert database entries into GeoJson format """
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Restaurants
        fields = ('id', 'name', 'address', 'image', 'tags', 'url_main', 'url_facebook',
                  'url_instagram', 'url_twitter', 'description_en', 'description_ge', 'description_ru')
        geo_field = 'location'
