import random
from typing import Tuple

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer


class RestaurantViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'patch', 'delete',)
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    filter_backends: Tuple = (SearchFilter,)
    search_fields: Tuple = ('name',)

    @action(detail=False, methods=('get',))
    def get_random_restaurant(self, request, *args, **kwargs):
        restaurants_count: int = self.queryset.count()
        random_id: int = random.choice(range(restaurants_count))
        serializer = self.serializer_class(self.queryset[random_id])
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
