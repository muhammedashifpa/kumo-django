from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import ProductTable
from .serializers import CartSerializer, CartSerializerForCreate, CheckoutCartSerializer
from .models import Cart
from django.db.models import Sum,F
from rest_framework.renderers import JSONRenderer
from products.models import Coupon

class CartView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = Cart.objects.filter(user=request.user)
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





class CheckoutCart(APIView):
    permission_classes = [IsAuthenticated]
    def get_data(self, request,**kwargs):
        coupon = kwargs.pop('coupon',None)
        queryset= Cart.objects.filter(user=request.user)
        serializer = CartSerializer(queryset,many=True , context={'request': request})
        sub_total = sum(i.get_total for i in queryset)
        tax = (sub_total/100)*8
        coupon_discount = 0
        if coupon is not None and sub_total + tax>=3000:
            coupon_obj = get_object_or_404(Coupon,coupon_code=coupon)
            if coupon_obj.is_valid:
                coupon_discount = 0-(sub_total/100)*coupon_obj.coupon_offer


        shipping_charge = 0 if sub_total + tax+coupon_discount >=7000 else 250

        total = sub_total+tax+shipping_charge+coupon_discount
        data = {'sub_total':sub_total,
                'tax':tax,
                'shipping_charge':shipping_charge,
                'coupon_discount':coupon_discount,
                'total':total,
                'items':serializer.data
                }
        return data
    
    def get(self,request,format=None,**kwargs):
        data = self.get_data(request,**kwargs)
        return Response(data)

    def post(self,request,format=None,**kwargs):
        print(request.data)
        kwargs['coupon']= request.data.get('coupon')
        data = self.get_data(request,**kwargs)
        return Response(data)
        
        














    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass


