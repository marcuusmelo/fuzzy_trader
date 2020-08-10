"""
Collection of functions to access external exchange info APIs
Note that this module access 3 different APIs. This is not ideal, as all the data can be found in
one of them (Alpha Vantage). But, as the free key for this API limits to 5 calls per minute, which
is too low, the design decision here was to continue using it as font of extra info for the
investments offered, and use 2 other APIs to get the real time rate.
"""
import os
import pytz
import requests
from datetime import datetime, timedelta

import django
django.setup()
from trader_simulator.models import CryptocurrencyInfo, StockInfo

class MarketData():
    """
    Collection of functions to access external exchange info APIs
    """

    def __init__(self):
        self.alpha_vantage_key = os.getenv('ALPHA_VANTAGE_KEY')
        self.coin_api_key = os.getenv('COIN_API_KEY')
        self.market_stack_key = os.getenv('MARKET_STACK_KEY')

    def get_cryptocurrency_rates(self, symbol):
        """
        Get cryptocurrency rates for a given symbol, from coinapi.io REST API
        """
        crypto_rate_url = 'https://rest.coinapi.io/v1/exchangerate/{0}/USD/?apikey={1}'
        request_url = crypto_rate_url.format(symbol, self.coin_api_key)
        response = requests.get(request_url)
        response_data = response.json()
        return response_data

    def get_cryptocurrency_info(self, symbol):
        """
        Get cryptocurrency info for a given symbol, from alpha vantage
        """
        now_datetime = datetime.now()
        now_datetime = now_datetime.replace(tzinfo=pytz.UTC)

        try:
            cryptocurrency_info = CryptocurrencyInfo.objects.values().filter(symbol__exact=symbol)[0]
        except IndexError:
            cryptocurrency_info = {}

        if not cryptocurrency_info or (now_datetime - cryptocurrency_info['source_datetime']) > timedelta(days=1):
            if cryptocurrency_info:
                CryptocurrencyInfo.objects.filter(symbol__exact=symbol).delete()

            crypto_info_url = "https://www.alphavantage.co/query?function=CRYPTO_RATING&symbol={0}&apikey={1}"
            request_url = crypto_info_url.format(symbol, self.alpha_vantage_key)
            response = requests.get(request_url)
            response_data = response.json()

            # format keys and select needed data
            cryptocurrency_info = {}
            cryptocurrency_info['symbol'] = response_data['Crypto Rating (FCAS)']['1. symbol']
            cryptocurrency_info['name'] = response_data['Crypto Rating (FCAS)']['2. name']
            cryptocurrency_info['fcas_rating'] = response_data['Crypto Rating (FCAS)']['3. fcas rating']
            cryptocurrency_info['fcas_score'] = response_data['Crypto Rating (FCAS)']['4. fcas score']
            cryptocurrency_info['source_datetime'] = now_datetime

            CryptocurrencyInfo(**cryptocurrency_info).save()

        return cryptocurrency_info

    def get_stock_rates(self, symbol):
        """
        Get stock rates for a given symbol, from market stack API
        """
        stock_rate_url = 'http://api.marketstack.com/v1/intraday/latest?symbols={0}&access_key={1}'
        request_url = stock_rate_url.format(symbol, self.market_stack_key)
        response = requests.get(request_url)
        response_data = response.json()
        return response_data

    def get_stock_info(self, symbol):
        """
        Get stock info for a given symbol, from alpha vantage
        """
        now_datetime = datetime.now()
        now_datetime = now_datetime.replace(tzinfo=pytz.UTC)

        try:
            stock_info = StockInfo.objects.values().filter(symbol__exact=symbol)[0]
        except IndexError:
            stock_info = {}

        if not stock_info or (now_datetime - stock_info['source_datetime']) > timedelta(days=1):
            if stock_info:
                StockInfo.objects.filter(symbol__exact=symbol).delete()

            stock_info_url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol={0}&apikey={1}"
            request_url = stock_info_url.format(symbol, self.alpha_vantage_key)
            response = requests.get(request_url)
            response_data = response.json()

            # format keys and select needed data
            stock_info = {}
            stock_info['symbol'] = response_data['Symbol']
            stock_info['name'] = response_data['Name']
            stock_info['gross_profit'] = response_data['GrossProfitTTM']
            stock_info['quartely_revenue_growth'] = response_data['QuarterlyRevenueGrowthYOY']
            stock_info['source_datetime'] = now_datetime

            StockInfo(**stock_info).save()

        return stock_info
