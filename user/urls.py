from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from django.contrib import admin
from django.urls import include , path
from .views import registration_view

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/' ,registration_view , name='register'),
]
