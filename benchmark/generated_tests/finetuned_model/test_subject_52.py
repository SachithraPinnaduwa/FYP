import unittest

class TestRebalanceFunction(unittest.TestCase):

    def test_rebalance_with_no_changes(self):
        # Test case when the current portfolio is already in the target allocation
        krypfolio = {'BTC': 0.5, 'ETH': 100, 'XRP': 1000}
        prices = {'BTC': 60000, 'ETH': 3000, 'XRP': 0.5}
        alloc = {'BTC': 10, 'ETH': 10, 'XRP': 80}
        investment = 100000
        updated_portfolio = rebalance(krypfolio, prices, alloc, investment)
        self.assertEqual(updated_portfolio, krypfolio)

    def test_rebalance_with_buy_operation(self):
        # Test case when the current portfolio needs to buy more cryptocurrencies
        krypfolio = {'BTC': 0.5, 'ETH': 100, 'XRP': 1000}
        prices = {'BTC': 60000, 'ETH': 3000, 'XRP': 0.5}
        alloc = {'BTC': 20, 'ETH': 10, 'XRP': 70}
        investment = 100000
        updated_portfolio = rebalance(krypfolio, prices, alloc, investment)
        self.assertGreater(updated_portfolio['BTC'], krypfolio['BTC'])
        self.assertGreater(updated_portfolio['ETH'], krypfolio['ETH'])
        self.assertGreater(updated_portfolio['XRP'], krypfolio['XRP'])

    def test_rebalance_with_sell_operation(self):
        # Test case when the current portfolio needs to sell some cryptocurrencies
        krypfolio = {'BTC': 0.5, 'ETH': 100, 'XRP': 1000}
        prices = {'BTC': 60000, 'ETH': 3000, 'XRP': 0.5}
        alloc = {'BTC': 10, 'ETH': 20, 'XRP': 70}
        investment = 100000
        updated_portfolio = rebalance(krypfolio, prices, alloc, investment)
        self.assertLess(updated_portfolio['BTC'], krypfolio['BTC'])
        self.assertLess(updated_portfolio['ETH'], krypfolio['ETH'])
        self.assertLess(updated_portfolio['XRP'], krypfolio['XRP'])

    def test_rebalance_with_full_rebalancing(self):
        # Test case when the current portfolio needs to buy and sell cryptocurrencies
        krypfolio = {'BTC': 0.5, 'ETH': 100, 'XRP': 1000}
        prices = {'BTC': 60000, 'ETH': 3000, 'XRP': 0.5}
        alloc = {'BTC': 20, 'ETH': 20, 'XRP': 60}
        investment = 100000
        updated_portfolio = rebalance(krypfolio, prices, alloc, investment)
        self.assertGreater(updated_portfolio['BTC'], krypfolio['BTC'])
        self.assertGreater(updated_portfolio['ETH'], krypfolio['ETH'])
        self.assertLess(updated_portfolio['XRP'], krypfolio['XRP'])