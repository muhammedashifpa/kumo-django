from django.urls import path,include
from .views import ProductSearch

app_name = 'search'

urlpatterns = [
    path('',ProductSearch.as_view(),name='search'),
]