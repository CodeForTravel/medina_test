from rest_framework.permissions import BasePermission


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin


class ConsumerOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_consumer

class VendorUserOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_vendor


class SuperAdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser



