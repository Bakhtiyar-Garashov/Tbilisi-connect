from rest_framework.response import Response
from .models import Restaurants, Tag, WelcomePage
from .serializer import RestaurantSerializer, TagSerializer, WelcomePageSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import status

class ListRestaurantsViewSet(viewsets.ViewSet):
    """
    Actions for Restaurants
    """

    def get_queryset(self):
        req = self.request
        name = req.query_params.get('name')
        tag = req.query_params.get('tag')
        if name and tag is None:
            self.queryset = Restaurants.objects.filter(name__istartswith=name)
            return self.queryset
        elif tag and name is None:
            self.queryset = Restaurants.objects.filter(tags__text=tag)
            return self.queryset
        else:
            self.queryset = Restaurants.objects.all()
            return self.queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = RestaurantSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Restaurants.objects.all()
        data = get_object_or_404(queryset, pk=pk)
        serialized = RestaurantSerializer(data, context={"request": request})
        return Response(serialized.data, status=status.HTTP_200_OK)

class ListAllTagsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class WelcomePageViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = WelcomePage.objects.all()
        serializer = WelcomePageSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data, status = status.HTTP_200_OK)
