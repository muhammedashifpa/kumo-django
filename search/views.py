from rest_framework import generics
from products.models import ProductTable
from products.serializers import ProductTableSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProductSearch(generics.ListAPIView):
    queryset = ProductTable.objects.all()
    serializer_class = ProductTableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['gender', 'product_name','brand']