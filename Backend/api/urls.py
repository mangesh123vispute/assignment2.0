from django.urls import path
from .views import StockDataViewSet

urlpatterns = [
    path('fetch', StockDataViewSet.as_view({'get': 'list'}), name='fetch'),
]
