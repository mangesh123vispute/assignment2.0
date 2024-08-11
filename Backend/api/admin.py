from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import StockData
from .resources import StockDataResource

# Define a resource class for import/export functionality


# Create a custom admin class for StockData
class StockDataAdmin(ImportExportModelAdmin):
    list_display = ('date', 'open', 'high', 'low', 'close', 'shares_traded', 'turnover')
    list_filter = ('date',)

# Register the model with the custom admin class
admin.site.register(StockData, StockDataAdmin)
