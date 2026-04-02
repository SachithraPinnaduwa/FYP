import unittest

class TestRebalance(unittest.TestCase):
    def test_rebalance(self):
        krypfolio = {'BTC': 0.5, 'ETH': 2.0, 'ADA': 100.0}
        prices = {'BTC': 50000, 'ETH': 3000, 'ADA': 1}
        alloc = {'BTC': 10, 'ETH': 20, 'ADA': 70}
        investment = 100000

        expected_result = {'BTC': 0.5001, 'ETH': 2.001, 'ADA': 99.99}
        self.assertAlmostEqual(rebalance(krypfolio, prices, alloc, investment), expected_result, places=3)

    def test_rebalance_with_zero_investment(self):
        krypfolio = {'BTC': 0.5, 'ETH': 2.0, 'ADA': 100.0}
        prices = {'BTC': 50000, 'ETH': 3000, 'ADA': 1}
        alloc = {'BTC': 10, 'ETH': 20, 'ADA': 70}
        investment = 0

        expected_result = {'BTC': 0.5, 'ETH': 2.0, 'ADA': 100.0}
        self.assertEqual(rebalance(krypfolio, prices, alloc, investment), expected_result)

    def test_rebalance_with_negative_investment(self):
        krypfolio = {'BTC': 0.5, 'ETH': 2.0, 'ADA': 100.0}
        prices = {'BTC': 50000, 'ETH': 3000, 'ADA': 1}
        alloc = {'BTC': 10, 'ETH': 20, 'ADA': 70}
        investment = -100000

        expected_result = {'BTC': 0.5, 'ETH': 2.0, 'ADA': 100.0}
        self.assertEqual(rebalance(krypfolio, prices, alloc, investment), expected_result)

    def test_rebalance_with_no_allocations(self):
        krypfolio = {'BTC': 0.5, 'ETH': 2.0, 'ADA': 100.0}
        prices = {'BTC': 50000, 'ETH': 3000, 'ADA': 1}
        alloc = {}
        investment = 100000

        expected_result = {'BTC': 0.5, 'ETH': 2.0, 'ADA': 100.0}
        self.assertEqual(rebalance(krypfolio, prices, alloc, investment), expected_result)

    def test_rebalance_with_empty_portfolio(self):
        krypfolio = {}
        prices = {'BTC': 50000, 'ETH': 3000, 'ADA': 1}
        alloc = {'BTC': 10, 'ETH': 20, 'ADA': 70}
        investment = 100000

        expected_result = {'BTC': 0.002, 'ETH': 0.006666666666666666, 'ADA': 33.333333333333336}
        self.assertAlmostEqual(rebalance(krypfolio, prices, alloc, investment), expected_result, places=3)

if __name__ == '__main__':
    unittest.main()