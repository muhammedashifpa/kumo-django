from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Favourite
from rest_framework.response import Response
from .serializers import FavouriteSerializer
from rest_framework.decorators import action
# Create your views here.

class FavouriteView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    # queryset = Favourite.objects.all()
    # model = Favourite
    # serializer_class = FavouriteSerializer
    # print(queryset)
    def list(self, request):
        queryset = Favourite.objects.filter(user=request.user.id)
        serializer = FavouriteSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def count(self, request):
        print(request.user.id)
        queryset = Favourite.objects.filter(user=request.user.id).count()
        return Response(queryset)