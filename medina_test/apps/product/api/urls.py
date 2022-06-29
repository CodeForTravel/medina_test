from rest_framework import routers
from django.urls import path, include
from medina_test.apps.product.api import views as product_views


router = routers.DefaultRouter()
router.register(r'weather-types', product_views.WeatherTypeViewSet, basename="weather-types")
router.register(r'category', product_views.ProductCategoryViewSet, basename="product-category")
router.register(r'products', product_views.ProductViewSet, basename="products")


urlpatterns = [
    path("", include(router.urls)),
]