from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from apps.bank import views

router = DefaultRouter()




router.register('schet', views.SchetViewSet),
router.register('action', views.ActionViewSet)
router.register('transfer', views.TransferViewSet)
router.register('transaction', views.TransactionViewset)

urlpatterns = [
    
    
    path('schets/', views.SchetListView.as_view())

]




urlpatterns += router.urls