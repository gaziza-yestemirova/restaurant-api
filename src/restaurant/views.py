from typing import Tuple

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer


class RestaurantViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'patch', 'delete',)
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    filter_backends: Tuple = (SearchFilter,)
    search_fields: Tuple = ('name',)
