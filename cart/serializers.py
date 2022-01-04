from django.db.models import Sum
from rest_framework import serializers

from products.models import ProductTable
from .models import Cart
from products.serializers import ProductTableSerializer
from accounts.serializers import CustomUserSerializer


class CartSerializer(serializers.ModelSerializer):
    user =  CustomUserSerializer()
    product =  ProductTableSerializer()
    class Meta:
        unique_together = [("user", "product","size")]
        model = Cart
        fields = '__all__'


class CartSerializerForCreate(serializers.ModelSerializer):
    class Meta:
        unique_together = [("user", "product","size")]
        model = Cart
        fields = '__all__'


class CheckoutCartSerializer(serializers.Serializer):
    sub_total = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    class Meta:
        fields = 'sub_total'

    def get_sub_total(self,obj):
        return 600
    def get_total(self,obj):
        return 500
        
