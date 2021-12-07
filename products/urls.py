from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductDetailView,ProductView

router = DefaultRouter()
router.register('', ProductView, basename='products')
urlpatterns = router.urls
app_name = 'products'

# urlpatterns = [
#     path('',ProductsListView.as_view()),
#     path('<pk>',ProductDetailView.as_view())
# ]