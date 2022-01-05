from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls', namespace='accounts')),
    path('product/',include('products.urls', namespace='products')),
    path('favourite/',include('favourite.urls', namespace='favourite')),
    path('api-auth/',include('rest_framework.urls', namespace='rest_frameworks')),
    path('cart/',include('cart.urls', namespace='cart')),
    path('payment/',include('payments.urls', namespace='payments')),
    path('order/',include('order.urls', namespace='order')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)