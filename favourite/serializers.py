from rest_framework import serializers
from .models import Favourite
from accounts.serializers import CustomUserSerializer
from products.serializers import ProductTableSerializer




class FavouriteSerializer(serializers.ModelSerializer):
    user =  CustomUserSerializer()
    product =  ProductTableSerializer()
    class Meta:
        unique_together = [("user", "product")]
        model = Favourite
        fields = '__all__'


class FavouriteSerializerForCreate(serializers.ModelSerializer):
    class Meta:
        unique_together = [("user", "product")]
        model = Favourite
        fields = '__all__'