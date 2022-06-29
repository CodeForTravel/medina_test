from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model

from medina_test.apps.user.api import serializers as serializers_user
from medina_test.apps.user.api import permissions as permissions_user


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & permissions_user.AdminOnly]
    queryset = User.objects.all()
    serializer_class = serializers_user.UserSerializer

