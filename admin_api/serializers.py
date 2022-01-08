from rest_framework import serializers
from accounts.models import NewUser
from order.models import Order, OrderItem
from order.serializers import OrderItemsSerializerForOrderList, OrderSerializerForGet
from datetime import datetime, timedelta

class AccountsSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(format="%d %b %H:%M")
    class Meta:
        model = NewUser
        fields = ('id','email','user_name', 'first_name','is_active','last_login')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields =[ 'id','first_name']


class OrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(format="%d %B %Y ")
    user = UserSerializer()
    expected_date = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = '__all__'
        depth = 2

    def get_expected_date(self,obj):
        
        return (obj.order_date+timedelta(days = 35)).strftime("%b %d %Y")
        
    def get_products(self,obj):
        request = self.context.get('request')
        return OrderItemsSerializerForOrderList(OrderItem.objects.filter(order=obj.id),many=True, context={'request': request}).data
