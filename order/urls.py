from django.urls import path
from .views import MyOrders


app_name = 'order'

urlpatterns = [
    path(r'',MyOrders.as_view(),name='my_order'),
]
