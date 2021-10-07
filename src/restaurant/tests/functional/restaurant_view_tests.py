from django.test import Client
from requests import Response

from restaurant.models import Restaurant


def test_restaurants_get_list_200(
        db, client: Client, restaurant_nicole: Restaurant,
        restaurant_peking_duck: Restaurant,
) -> None:
    response: Response = client.get(path='/api/restaurants/')

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


def test_restaurants_retrieve_by_id_200(
        db, client: Client, restaurant_nicole: Restaurant,
) -> None:
    response: Response = client.get(path=f'/api/restaurants/{restaurant_nicole.pk}/')

    assert response.status_code == 200 and response.json() == {
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
        )
    }


def test_restaurants_delete_204(
        db, client: Client, restaurant_nicole: Restaurant,
) -> None:
    response: Response = client.delete(path=f'/api/restaurants/{restaurant_nicole.pk}/')

    assert response.status_code == 204
    assert Restaurant.objects.count() == 0


def test_restaurants_create_201_and_update_200(
    db, client: Client,
) -> None:
    restaurant_data = {
        'name': 'Sababa',
        'state': Restaurant.CLOSED,
        'address': 'Zhambyl St 144, Almaty',
        'phone': '+77013335333',
        'cuisine': 'Greece',
    }
    response: Response = client.post(
        path='/api/restaurants/',
        data=restaurant_data,
        content_type='application/json',
    )
    assert response.status_code == 201
    restaurant_pk: str = response.json()['id']
    restaurant_sababa: Restaurant = Restaurant.objects.filter(
        id=restaurant_pk
    ).last()
    assert restaurant_sababa.rating == 0

    new_rating: int = 5
    response = client.patch(
        path=f'/api/restaurants/{restaurant_pk}/',
        data={'rating': new_rating},
        content_type='application/json',
    )
    assert response.status_code == 200
    restaurant_sababa.refresh_from_db()
    assert restaurant_sababa.rating == new_rating
