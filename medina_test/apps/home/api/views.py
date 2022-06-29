from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from medina_test.apps.home.api import serializers as serializers_home
from medina_test.apps.user.api import permissions as permissions_user
from medina_test.apps.home import models as models_home


class WeatherTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & permissions_user.AdminOnly]
    queryset = models_home.WeatherType.objects.all()
    serializer_class = serializers_home.WeatherTypeSerializer