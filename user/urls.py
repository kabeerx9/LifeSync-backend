from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

from django.urls import   path
from .views import registration_view
from .tokens import CustomTokenObtainPairView

urlpatterns = [
     path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/register/' ,registration_view , name='register'),
]
