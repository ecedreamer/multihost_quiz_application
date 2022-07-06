from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import *


app_name = "api_server"

urlpatterns = [
    path("login", UserLoginAPIView.as_view()),
    path('refresh-token', TokenRefreshView.as_view()),
    path('profile', UserProfileAPIView.as_view()),
    
]