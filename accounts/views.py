from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,BasePermission
from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer,UserProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import NewUser

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_name = request.user.user_name
        # print(user_name)
        data = get_object_or_404(NewUser,user_name=user_name)
        serialized = UserProfileSerializer(data)
        return Response(serialized.data,status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        pass

    def delete(self, request):
        pass
    
    def patch(self, request):
        user_name = request.user.user_name
        user = get_object_or_404(NewUser,user_name=user_name)
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'success'},status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
