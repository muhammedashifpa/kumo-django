from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Favourite
from rest_framework.response import Response
from .serializers import FavouriteSerializer,FavouriteSerializerForCreate
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from products.models import ProductTable
from products.serializers import ProductTableSerializer
# Create your views here.

class FavouriteView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset_one = Favourite.objects.filter(user=request.user.id)
        serializer = FavouriteSerializer(queryset_one, many=True, context={'request': request})
        # queryset_one = Favourite.objects.filter(user=request.user.id).values_list('product', flat=True)
        # queryset = ProductTable.objects.filter(id__in=queryset_one)
        # serializer = ProductTableSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = FavouriteSerializerForCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'success','data':serializer.data})
        print(serializer.errors)
        return Response({'message':'error','data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Favourite,pk=pk)
        serializer = FavouriteSerializer(queryset)
        return Response(serializer.data)
        

    def destroy(self, request, pk=None):
        queryset = get_object_or_404(Favourite,pk=pk).delete()
        serializer = FavouriteSerializerForCreate(queryset)
        return Response({'message':'delete success','data':serializer.data})
    
    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass
