from django.shortcuts import render
from apps.user.serializers import UserSerializer
from apps.user.models import User
from rest_framework import generics

class UserApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer