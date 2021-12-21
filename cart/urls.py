from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import CartView


router = DefaultRouter()
router.register('',CartView,basename='cart')
urlpatterns = router.urls
app_name = 'cart'
