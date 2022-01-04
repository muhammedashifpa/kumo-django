from django.urls import path

from .views import *
app_name = 'payments'
urlpatterns = [
    path('pay/', start_payment, name="payment"),
    path('success/', handle_payment_success, name="payment_success")
]