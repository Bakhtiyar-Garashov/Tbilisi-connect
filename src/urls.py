
from typing import DefaultDict
from django.urls import path
from .views import ListRestaurantsViewSet
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ListRestaurantsViewSet, basename='Restaurants')

urlpatterns= [
    path('restaurants/', include(router.urls))
]