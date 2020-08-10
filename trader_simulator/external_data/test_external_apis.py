import unittest
from trader_simulator.external_data.exchange_apis import MarketData

class TestsMarketData(unittest.TestCase):
    def setUp(self):
        self.market_data = MarketData()

    def test_get_cryptocurrency_rates(self):
        bitcoin_rate = self.market_data.get_cryptocurrency_rates('BTC')
        self.assertEqual(bitcoin_rate['asset_id_base'], 'BTC')

    def test_get_cryptocurrency_info(self):
        bitcoin_info = self.market_data.get_cryptocurrency_info('BTC')
        self.assertEqual(bitcoin_info['name'], 'Bitcoin')

    def test_get_stock_rate(self):
        apple_rate = self.market_data.get_stock_rates('AAPL')
        self.assertEqual(type(apple_rate['data'][0]['last']), float)

    def test_get_stock_info(self):
        apple_info = self.market_data.get_stock_info('AAPL')
        self.assertEqual(apple_info['name'], 'Apple Inc')


if __name__ == '__main__':
    unittest.main()
