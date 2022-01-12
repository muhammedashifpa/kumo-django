from rest_framework import viewsets, status,filters
from rest_framework.decorators import parser_classes
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from products.models import ProductTable
from products.serializers import FullTable, ProductTableSerializer
from rest_framework.permissions import IsAdminUser
from accounts.models import NewUser
from order.models import Order
from .serializers import OrderSerializer,AccountsSerializer
from rest_framework.response import Response
from datetime import datetime, timedelta
from rest_framework.parsers import MultiPartParser,FileUploadParser,FormParser
from products.models import Images



class AccountView(viewsets.ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = AccountsSerializer
    permission_classes = [IsAdminUser]


class ProductsView(viewsets.ModelViewSet):
    queryset = ProductTable.objects.all()
    serializer_class = ProductTableSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.OrderingFilter]
    ordering = ['-id']

class ProductImage(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser,FormParser]
    def post(self, request):
        serializers = FullTable(data=request.data)
        if serializers.is_valid():
            serializers.save()
            print(serializers.data)
            return Response(serializers.data,status=200)
        return Response(status=400,data={'helooo':'heeooo'})

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]


def get_date_of_order():
    today = datetime.now().date()
    dates = [today-timedelta(i) for i in range(7)]
    data = []
    for date in dates:
        data.insert(0,{
            'name': str(date.strftime('%b %d')),
            'count':  Order.objects.filter(order_date__range=[date-timedelta(1),date]).count()
            })
        print(data)
    return data



class OrderDetails(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        data = get_date_of_order()
        return Response(data)

def get_date_of_user():
    today = datetime.now().date()
    dates = [today-timedelta(i) for i in range(7)]
    data = []
    for date in dates:
        data.insert(0,{
            'name': str(date.strftime('%b %d')),
            'count':  NewUser.objects.filter(start_date__range=[date-timedelta(1),date]).count()
            })
    return data

class UserDetails(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        data = get_date_of_user()
        print(data)
        return Response(data)
