from rest_framework.routers import DefaultRouter
from .views import FavouriteView

app_name = 'favourite'
router = DefaultRouter()
router.register('', FavouriteView, basename='favourite')
urlpatterns = router.urls