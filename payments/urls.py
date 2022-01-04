from django.urls import path
from .views import MakePayment, saveStripeInfo, OrderPlace
from rest_framework.routers import DefaultRouter

app_name = 'payments'

urlpatterns = [
    path('', MakePayment.as_view(), name ='make-payment'),
    path('place-order', OrderPlace.as_view(), name ='place-order'),
    path(r'save-stripe-info/', saveStripeInfo.as_view(), name ='save-stripe-info'),


]
