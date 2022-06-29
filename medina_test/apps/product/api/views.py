from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from medina_test.apps.product.api import serializers as serializers_product
from medina_test.apps.user.api import permissions as permissions_user
from medina_test.apps.product import models as models_product


class WeatherTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & permissions_user.AdminOnly]
    queryset = models_product.WeatherType.objects.all()
    serializer_class = serializers_product.WeatherTypeSerializer