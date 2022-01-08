from rest_framework.routers import DefaultRouter
from .views import ProductsView, AccountView, OrderView

router = DefaultRouter()
router.register('products', ProductsView, basename='product')
router.register('orders', OrderView, basename='order')
router.register('accounts', AccountView, basename='account')
urlpatterns = router.urls
app_name = 'admiin_api'