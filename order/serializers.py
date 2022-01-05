from rest_framework import serializers
from .models import Order, OrderItem
from accounts.serializers import CustomUserSerializer
from products.serializers import ProductTableSerializer,FullTable
from datetime import datetime, timedelta


class OrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(format="%d %B %Y %I : %M %p")
    user = CustomUserSerializer()
    class Meta:
        model = Order
        fields = '__all__'
        depth = 2


class OrderItemsSerializerForOrderList(serializers.ModelSerializer):
    product = ProductTableSerializer()
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializerForGet(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(format="%d %B %Y")
    user = CustomUserSerializer()
    products = serializers.SerializerMethodField()
    expected_date = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = '__all__'
        depth = 2

    def get_expected_date(self,obj):
        print(obj.order_date+timedelta(days = 35))
        print()
        print(obj.order_date)
        print('***************')
        
        return (obj.order_date+timedelta(days = 35)).strftime("%b %d %Y")
        
    def get_products(self,obj):
        request = self.context.get('request')
        return OrderItemsSerializerForOrderList(OrderItem.objects.filter(order=obj.id),many=True, context={'request': request}).data


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemsSerializerForGet(serializers.ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = OrderItem
        fields = '__all__'