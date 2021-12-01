from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import CustomUserCreate, HelloView, BlacklistTokenUpdateView, MyTokenObtainPairView, ProfileDetailView


app_name = 'accounts'

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('register/',CustomUserCreate.as_view(),name='register'),
    path('logout/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('', HelloView.as_view()),
    path('user/',ProfileDetailView.as_view(),name='profile_detail'),

]
