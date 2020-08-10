import unittest
from trader_simulator.external_data.exchange_apis import MarketData
from trader_simulator.external_data.exchange_apis_config import AVAILABLE_INVESTMENTS

class TestsMarketData(unittest.TestCase):
    def setUp(self):
        self.market_data = MarketData()

    def test_get_cryptocurrency_rates(self):
        bitcoin_rate = self.market_data._get_cryptocurrency_rates('BTC')
        self.assertEqual(bitcoin_rate['asset_id_base'], 'BTC')

    def test_get_cryptocurrency_info(self):
        bitcoin_info = self.market_data._get_cryptocurrency_info('BTC')
        self.assertEqual(bitcoin_info['name'], 'Bitcoin')

    def test_get_stock_rate(self):
        apple_rate = self.market_data._get_stock_rates('AAPL')
        self.assertEqual(type(apple_rate['data'][0]['last']), float)

    def test_get_stock_info(self):
        apple_info = self.market_data._get_stock_info('AAPL')
        self.assertEqual(apple_info['name'], 'Apple Inc')

    def test_get_value(self):
        apple_value = self.market_data.get_value('AAPL', 10)
        self.assertEqual(type(apple_value), float)

    def test_get_rate(self):
        apple_rate = self.market_data.get_rate('AAPL')
        self.assertEqual(type(apple_rate), float)

    def test_get_info(self):
        symbol = 'AAPL'
        apple_info = self.market_data.get_info(symbol)
        self.assertEqual(apple_info['name'], 'Apple Inc')

    def test_get_all_data(self):
        all_info = self.market_data.get_all_data()
        all_symbols = []
        for investment_type, symbol_list in AVAILABLE_INVESTMENTS.items():
            all_symbols += symbol_list
        self.assertEqual(len(all_info), len(all_symbols))


if __name__ == '__main__':
    unittest.main()
