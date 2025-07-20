from django.urls import path
from .views import RegisterView, GoogleLogin

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('google/login/', GoogleLogin.as_view(), name='google_login'),
]
