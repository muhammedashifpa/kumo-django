from rest_framework.views import APIView
from .models import ProductTable
from .serializers import ProductTableSerializer
from rest_framework import response, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, IsAuthenticated
from rest_framework import status

# Create your views here.
class ReadOnly(BasePermission):
    ''''Admin or Read only'''
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class ProductView(viewsets.ModelViewSet,ReadOnly):
    permission_classes = [IsAdminUser|ReadOnly]
    serializer_class = ProductTableSerializer

    def get_queryset(self):
        return ProductTable.objects.all()

    def get_object(self, queryset=None, **kwargs):
        slug = self.kwargs.get('pk')
        obj = get_object_or_404(ProductTable, slug=slug)
        return obj

class CategoryView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, gender, format=None):
        queryset = ProductTable.objects.filter(gender__iexact=gender)
        serializers = ProductTableSerializer(queryset,many=True, context={'request': request})
        return Response(status=status.HTTP_200_OK,data=serializers.data)
