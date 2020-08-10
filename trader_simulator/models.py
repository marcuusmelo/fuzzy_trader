from django.db import models


class CryptocurrencyInfo(models.Model):
    symbol = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=128)
    fcas_rating = models.CharField(max_length=64)
    fcas_score = models.FloatField()
    source_datetime = models.DateTimeField()

class StockInfo(models.Model):
    symbol = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=128)
    gross_profit = models.FloatField()
    quartely_revenue_growth = models.FloatField()
    source_datetime = models.DateTimeField()

class InvestmentLog(models.Model):
    username = models.CharField(max_length=128)
    investment_symbol = models.CharField(max_length=32)
    quantity = models.IntegerField()
