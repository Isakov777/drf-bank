from django.db import transaction
from django.http import request
from django.utils import translation, tree
from rest_framework import authentication
from rest_framework import serializers
from rest_framework import permissions
from rest_framework import views
from rest_framework.decorators import authentication_classes

from rest_framework.serializers import Serializer
# from apps.bank.mixins import ServiceExcrptionHandleMixin
from apps.bank.serializers import ActionSerializer, SchetSerializer, TransferSerializer, TransactionSerializer
from apps.bank.models import Action, Schet, Transaction, Transfer
from apps.user.models import User
from rest_framework import generics,viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.bank.services import make_transfer
from rest_framework.views import APIView
from django.db.transaction import atomic

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

# class UserCreateViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class CustomerDetail(generics.RetrieveUpdateAPIView):
    serializer_class = SchetSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Schet.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user = request.user)






class SchetListView(generics.ListAPIView):
    serializer_class = SchetSerializer
    queryset = Schet.objects.all()


class SchetViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = SchetSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Schet.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(user = request.user)

    def get_queryset(self):
        
        return self.queryset.filter(user = self.request.user)




class ActionViewSet(viewsets.ModelViewSet):
    serializer_class = ActionSerializer
    
    queryset = Action.objects.all()


  
class TransferViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = TransferSerializer
    queryset = Transfer.objects.all()
    # authentication_classes = (TokenAuthentication)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        try:
            make_transfer(**serializer.validated_data)
        except ValueError:
            content = {'error': 'Not enough money'}
            return Response(content, status = status.HTTP_400_BAD_REQUEST)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status = status.HTTP_201_CREATED, headers = headers)







class TransactionViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        try:
            schet = Schet.objects.filter(
                user = self.request.user).get(pk = self.request.data['schet'])
        except Exception as e:
            print(e)
            content = {'error': 'Not such schet'}
            return Response(content, status = status.HTTP_400_BAD_REQUEST)

        serializer.save(schet = schet)

        try:
            Transaction.make_transaction(**serializer.validated_data)
        except ValueError:
            content = {'error': 'Not enough money'}
            return Response(content, status = status.HTTP_400_BAD_REQUEST)


        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status= status.HTTP_201_CREATED, headers=headers)

    # def get_queryset(self):
    #     schets = Schet.objects.filter(user = request.user)
    #     return self.queryset.filter(schet__in = schets)