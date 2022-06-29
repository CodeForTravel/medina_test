from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from medina_test.apps.product.api import filters as filters_product
from medina_test.apps.product.api import serializers as serializers_product
from medina_test.apps.user.api import permissions as permissions_user
from medina_test.apps.product import models as models_product
from medina_test.apps.user.api import pagination as pagination_global

class WeatherTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & permissions_user.AdminOnly]
    queryset = models_product.WeatherType.objects.all()
    serializer_class = serializers_product.WeatherTypeSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & permissions_user.AdminOnly]
    queryset = models_product.ProductCategory.objects.all()
    serializer_class = serializers_product.ProductCategorySerializer



class ProductViewSet(viewsets.ModelViewSet):
    queryset = models_product.Product.objects.all()
    serializer_class = serializers_product.ProductSerializer
    pagination_class = pagination_global.GlobalPagination

    filter_backends = [
        filters.SearchFilter,
        filters_product.ProductFilterBackend,
    ]
    search_fields = [
        "name",
        "weather_type__name",
    ]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ["retrieve", "list"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated & permissions_user.VendorUserOnly]
        return [permission() for permission in permission_classes]