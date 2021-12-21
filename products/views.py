from .models import ProductTable
from .serializers import ProductTableSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductTableSerializer
    def get_queryset(self):
        return ProductTable.objects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(ProductTable, slug=item)
