from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer
from .models import CustomUser
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
