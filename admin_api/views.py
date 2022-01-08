from rest_framework import viewsets
from products.models import ProductTable
from products.serializers import ProductTableSerializer
from rest_framework.permissions import IsAdminUser
from accounts.models import NewUser
from accounts.serializers import UserProfileSerializer
from order.models import Order
from order.serializers import OrderSerializerForGet
from .serializers import OrderSerializer,AccountsSerializer
import time



class AccountView(viewsets.ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = AccountsSerializer
    permission_classes = [IsAdminUser]


class ProductsView(viewsets.ModelViewSet):
    queryset = ProductTable.objects.all()
    serializer_class = ProductTableSerializer
    permission_classes = [IsAdminUser]

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
