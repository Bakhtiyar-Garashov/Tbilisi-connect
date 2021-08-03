
from typing import DefaultDict
from django.urls import path
from .views import ListRestaurantsViewSet, ListAllTagsViewSet
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'restaurants', ListRestaurantsViewSet, basename='Restaurants')
router.register(r'tags', ListAllTagsViewSet, basename='Tags')


urlpatterns= [
    path('', include(router.urls))
]