from rest_framework import serializers
from .models import ProductTable,SizeType,Images



class FullTable(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class ProductTableSerializer(serializers.ModelSerializer):
    images = FullTable(many=True, read_only=True)
    class Meta:
        model = ProductTable
        fields = '__all__'
