from rest_framework import viewsets
from .models import StockData
from .serializers import StockDataSerializer

class StockDataViewSet(viewsets.ModelViewSet):
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer
