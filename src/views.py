from rest_framework.response import Response
from .models import Restaurants, Tag
from .serializer import RestaurantSerializer
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
        if name:
            self.queryset = Restaurants.objects.filter(name=name)
            return self.queryset
        else:
            self.queryset = Restaurants.objects.all()
            return self.queryset

    def list(self, request):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = RestaurantSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        queryset = Restaurants.objects.all()
        data = get_object_or_404(queryset, pk=pk)
        serialized = RestaurantSerializer(data)
        return Response(serialized.data, status=status.HTTP_200_OK)
