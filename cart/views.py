from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from products.models import ProductTable
from .serializers import CartSerializer, CartSerializerForCreate
from .models import Cart
from django.db.models import Sum

class CartView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = Cart.objects.filter(user=request.user)
        print(ProductTable.objects.filter(product__in=queryset).aggregate(Sum('price')))
        serializer = CartSerializer(queryset,many=True , context={'request': request})
        return Response(serializer.data)


    def create(self, request):
        if int(request.data['user']) != request.user.id:
            return Response({'message':'UnAuthenticated'})
        serializer = CartSerializerForCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'success','data':serializer.data})
        return Response({'message':'error','data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        queryset = get_object_or_404(Cart,pk=pk).delete()
        return Response({'message':'delete success'})


    def partial_update(self, request, pk=None):
        instance = get_object_or_404(Cart,pk=pk)
        # print(request.user.user_name,instance.user.user_name)
        if instance.user.user_name != request.user.user_name:
            return Response({'message':'UnAuthenticated'}, status=status.HTTP_400_BAD_REQUEST)
        serialized = CartSerializerForCreate(instance, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response({'message':'success','data':serialized.data})
        return Response({'message':'error','data':serialized.errors}, status=status.HTTP_400_BAD_REQUEST)

        















    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass


