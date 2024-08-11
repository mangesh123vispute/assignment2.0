from django.db import models


class StockData(models.Model):
    date = models.CharField(max_length=20)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    shares_traded = models.BigIntegerField()
    turnover = models.DecimalField(max_digits=15, decimal_places=2)

   
    def __str__(self):
        return f"Data for {self.date}"