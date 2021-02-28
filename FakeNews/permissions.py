from rest_framework.permissions import IsAdminUser, SAFE_METHODS
from django.contrib import admin
from django.contrib.auth.models import Group, User

# disable user and group creation
admin.site.unregister(Group)
admin.site.unregister(User)


class IsAdminUserOrReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin
