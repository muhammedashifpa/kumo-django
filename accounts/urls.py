from django.urls import path
from django.views.generic import TemplateView
from rest_framework_simplejwt import views as jwt_views
from .views import CustomUserCreate, HelloView


app_name = 'accounts'

urlpatterns = [
    path('', HelloView.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('register/',CustomUserCreate.as_view(),name='register'),

]
