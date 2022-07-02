import ast
from gettext import install
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from constance import config as constance_config


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
        if self.action in ["retrieve", "list", "product_recommendation"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated & permissions_user.VendorUserOnly]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['get'], url_path="recommendations")
    def product_recommendation(self, request):

        weather_data = constance_config.WEATHER_DATA
        weather_data = dict(ast.literal_eval(weather_data))
        current_temp = int(weather_data.get('temp'))
        weather_objs = models_product.WeatherType.objects.all()
        filtered_weather_objs = []
        for obj in weather_objs:
            if current_temp >= obj.low_temp and current_temp<= obj.high_temp:
                filtered_weather_objs.append(obj)

        products = self.get_queryset().filter(weather_type__in=filtered_weather_objs)
        serializer = serializers_product.ProductSerializer(products,many=True)
        return Response({'data': serializer.data},status=status.HTTP_200_OK)
 
        