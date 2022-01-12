from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from .serializers import OrderSerializerForGet, OrderItemsSerializerForGet

class MyOrders(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset_one = Order.objects.filter(user=request.user).order_by('-id')
        serializer = OrderSerializerForGet(queryset_one,many=True, context={'request': request})
        return Response(serializer.data)
