from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import  ProductView, ProductDetailView

app_name = 'products'
urlpatterns = [
    path('', ProductView.as_view(), name='product-list'),
    path('<str:slug>', ProductDetailView.as_view(), name='product-detail'),
]

