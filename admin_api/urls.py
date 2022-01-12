from rest_framework.routers import DefaultRouter
from .views import ProductsView, AccountView, OrderView, OrderDetails,UserDetails,ProductImage
from django.urls import path,include


router = DefaultRouter()
router.register('products', ProductsView, basename='product')
router.register('orders', OrderView, basename='order')
router.register('accounts', AccountView, basename='account')
urlpatterns = [
    path('order-detail',OrderDetails.as_view(),name='order-detail'),
    path('user-detail',UserDetails.as_view(),name='user-detail'),
    path('product-image',ProductImage.as_view(),name='product-image'),
    path('',include(router.urls))
]
app_name = 'admiin_api'