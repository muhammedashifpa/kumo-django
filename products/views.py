from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import ProductTable,SizeType
from rest_framework import generics
from .serializers import ProductTableSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductTableSerializer
    def get_queryset(self):
        return ProductTable.objects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(ProductTable, slug=item)




class ProductDetailView(DetailView):
    model = ProductTable
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['producttable'].size_type)
        size_type = context['producttable'].size_type
        a = SizeType.objects.get(size_types=size_type)
        a.size_set.all()
        print(a.size_set.all())
        context['book_list'] = a.size_set.all()
        return context