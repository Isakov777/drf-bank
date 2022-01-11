from django.urls import path
from apps.user.views import UserApiView
from rest_framework import urlpatterns

urlpatterns = [
    path('', UserApiView.as_view(), name = 'user')
]
