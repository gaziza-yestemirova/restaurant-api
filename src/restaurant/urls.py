from rest_framework.routers import DefaultRouter

from restaurant.views import RestaurantViewSet

router = DefaultRouter()
router.register(
    prefix='restaurants', viewset=RestaurantViewSet, basename='restaurants',
)
urlpatterns = router.urls
