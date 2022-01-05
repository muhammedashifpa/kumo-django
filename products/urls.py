from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductView, CategoryView

app_name = 'products'
router = DefaultRouter()
# router.register('category', CategoryView, basename='category')
router.register('', ProductView, basename='products')
urlpatterns = [
    # path('category', CategoryView.as_view(), name='category'),
    path('category/<str:gender>/', CategoryView.as_view(), name='category'),
    path('',include(router.urls))
]
# urlpatterns = router.urls

