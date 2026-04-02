from subject_52 import *

import unittest

class TestRebalance(unittest.TestCase):
    def test_normal_case(self):
        krypfolio = {'BTC': 0.5, 'ETH': 0.3, 'LTC': 0.2}
        prices = {'BTC': 30000, 'ETH': 1500, 'LTC': 100}
        alloc = {'BTC': 50, 'ETH': 30, 'LTC': 20}
        investment = 100000
        expected = {'BTC': 0.5, 'ETH': 0.3, 'LTC': 0.2}  # Expected output after rebalancing
        self.assertEqual(rebalance(krypfolio, prices, alloc, investment), expected)

    def test_edge_case_empty_portfolio(self):
        krypfolio = {}
        prices = {'BTC': 30000, 'ETH': 1500, 'LTC': 100}
        alloc = {'BTC': 50, 'ETH': 30, 'LTC': 20}
        investment = 100000
        expected = {'BTC': 0.5, 'ETH': 0.3, 'LTC': 0.2}  # Expected output after rebalancing
        self.assertEqual(rebalance(krypfolio, prices, alloc, investment), expected)

    def test_edge_case_empty_allocation(self):
        krypfolio = {'BTC': 0.5, 'ETH': 0.3, 'LTC': 0.2}
        prices = {'BTC': 30000, 'ETH': 1500, 'LTC': 100}
        alloc = {}
        investment = 100000
        expected = {'BTC': 0.5, 'ETH': 0.3, 'LTC': 0.2}  # Expected output after rebalancing
        self.assertEqual(rebalance(krypfolio, prices, alloc, investment), expected)

    def test_error_handling_negative_investment(self):
        krypfolio = {'BTC': 0.5, 'ETH': 0.3, 'LTC': 0.2}
        prices = {'BTC': 30000, 'ETH': 1500, 'LTC': 100}
        alloc = {'BTC': 50, 'ETH': 30, 'LTC': 20}
        investment = -100000
        with self.assertRaises(ValueError) as context:
            rebalance(krypfolio, prices, alloc, investment)
        self.assertEqual(str(context.exception), 'Investment amount must be non-negative.')

if __name__ == '__main__':
    unittest.main()