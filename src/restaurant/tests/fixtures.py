from pytest import fixture

from restaurant.models import Restaurant


@fixture
def restaurant_nicole() -> Restaurant:
    return Restaurant.objects.create(
        name='Nicole', state=Restaurant.OPEN,
        address='34433 Beyoglu, Istanbul', rating=5,
        phone='+902122924467', cuisine='French',
        is_active=True,
    )


@fixture
def restaurant_peking_duck() -> Restaurant:
    return Restaurant.objects.create(
        name='J.Z. Peking Duck', state=Restaurant.OPEN,
        address='Shashkin St 1, Almaty', rating=4,
        phone='+77057730808', cuisine='Chinese',
        is_active=True,
    )
