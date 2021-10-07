from rest_framework import serializers
from restaurant.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = (
            'id', 'name', 'state', 'address', 'rating', 'phone', 'cuisine',
            'created', 'modified',
        )
