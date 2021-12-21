from rest_framework import serializers
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