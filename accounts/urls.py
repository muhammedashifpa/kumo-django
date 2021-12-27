from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import CustomUserCreate, BlacklistTokenUpdateView, MyTokenObtainPairView, ProfileView,AddressView
from rest_framework import routers
from rest_framework.routers import DefaultRouter

app_name = 'accounts'

router = DefaultRouter()
router.register(r'address', AddressView, basename='address')
urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('register/',CustomUserCreate.as_view(),name='register'),
    path('logout/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('user/',ProfileView.as_view(),name='profile_detail'),

]+router.urls
