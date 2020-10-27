"""django_login URL Configuration
"""
from django.contrib import admin
import django_prometheus.urls
from django.urls import path, include
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/v1/token-auth/', obtain_jwt_token),
    path(r'api/v1/token-refresh/', refresh_jwt_token),
    path(r'api/v1/token-verify/', verify_jwt_token),
    path('', include('django_prometheus.urls')),
]
