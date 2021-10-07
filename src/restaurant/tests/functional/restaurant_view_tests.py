from django.test import Client

from restaurant.models import Restaurant


def test_restaurants_get_list_200(
    db, client: Client, restaurant_nicole: Restaurant,
    restaurant_peking_duck: Restaurant,
) -> None:
    response = client.get(path='/api/restaurants/')

    assert response.status_code == 200
    assert response.json() == {
        'count': 2,
        'next': None,
        'previous': None,
        'results': [{
            'id': restaurant_nicole.pk,
            'name': restaurant_nicole.name,
            'state': restaurant_nicole.state,
            'address': restaurant_nicole.address,
            'rating': restaurant_nicole.rating,
            'phone': restaurant_nicole.phone,
            'cuisine': restaurant_nicole.cuisine,
            'created': restaurant_nicole.created.strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'modified': restaurant_nicole.modified.strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
        }, {
            'id': restaurant_peking_duck.pk,
            'name': restaurant_peking_duck.name,
            'state': restaurant_peking_duck.state,
            'address': restaurant_peking_duck.address,
            'rating': restaurant_peking_duck.rating,
            'phone': restaurant_peking_duck.phone,
            'cuisine': restaurant_peking_duck.cuisine,
            'created': restaurant_peking_duck.created.strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'modified': restaurant_peking_duck.modified.strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
        }],
    }
