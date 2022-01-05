from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import CartView, CheckoutCart


router = DefaultRouter()
router.register('',CartView,basename='cart')
# router.register('checkout-cart/',CheckoutCart,basename='checkout-cart')
# urlpatterns = router.urls
app_name = 'cart'
urlpatterns = [
    path(r'checkout-cart/',CheckoutCart.as_view(),name='checkout_cart'),
    path('',include(router.urls))
]
