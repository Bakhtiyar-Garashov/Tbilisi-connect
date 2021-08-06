from rest_framework_gis import serializers as geoserializers
from rest_framework import serializers
from .models import Restaurants, Tag, WelcomePage


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('text',)


class RestaurantSerializer(geoserializers.GeoFeatureModelSerializer):
    """ Convert database entries into GeoJson format """
    tags = TagSerializer(read_only=True, many=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Restaurants
        fields = ('id', 'name', 'address', 'image_url', 'tags', 'crypto_payment_option', 'url_main', 'url_facebook',
                  'url_instagram', 'url_twitter', 'url_google_map', 'description_en', 'description_ge', 'description_ru')
        geo_field = 'location'

    def get_image_url(self, restaurant):
        request = self.context.get('request')
        photo_url = restaurant.image.url
        return request.build_absolute_uri(photo_url)


class WelcomePageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = WelcomePage
        fields = ('id', 'title', 'subtitle_en', 'subtitle_ge', 'subtitle_ru', 'image_url', 'url_main', 'url_facebook',
                  'url_instagram', 'url_twitter')

    def get_image_url(self, welcomepage):
        request = self.context.get('request')
        photo_url = welcomepage.image.url
        return request.build_absolute_uri(photo_url)
