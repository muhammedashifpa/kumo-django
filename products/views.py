from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.views import APIView
from .models import ProductTable
from .serializers import ProductTableSerializer
from rest_framework import generics, response, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework import filters
from django.db import connection
from django.db.models import Q


# Create your views here.
class ReadOnly(BasePermission):
    ''''Admin or Read only'''
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS



class ProductDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser|ReadOnly]
    serializer_class = ProductTableSerializer
    lookup_field = 'slug'
    queryset = ProductTable.objects.all()

class ProductView(generics.ListAPIView):
    queryset = ProductTable.objects.all()
    serializer_class = ProductTableSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['gender', 'product_name','brand']
    search_fields = ['=gender' ,'$category','product_name','brand__brand']

































# class ProductView(viewsets.ModelViewSet,ReadOnly):
#     permission_classes = [IsAdminUser|ReadOnly]
#     serializer_class = ProductTableSerializer

#     def get_queryset(self):
#         return ProductTable.objects.all()

#     def get_object(self, queryset=None, **kwargs):
#         slug = self.kwargs.get('pk')
#         obj = get_object_or_404(ProductTable, slug=slug)
#         return obj



# class ProductListView(generics.ListAPIView):
#     permission_classes = [IsAdminUser|ReadOnly]
#     serializer_class = ProductTableSerializer
#     queryset = ProductTable.objects.all()
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['=gender' ,'$category','product_name','brand__brand']