from import_export import resources
from .models import StockData

class StockDataResource(resources.ModelResource):
    class Meta:
        model = StockData
        fields = ('date', 'open', 'high', 'low', 'close', 'shares_traded', 'turnover')
        import_id_fields = ('date',)
