from subject_52 import *

import unittest

class TestRebalance(unittest.TestCase):
    def test_rebalance(self):
        krypfolio = {'BTC': 0.5, 'ETH': 1.0, 'XRP': 100.0}
        prices = {'BTC': 40000, 'ETH': 3000, 'XRP': 1.5}
        alloc = {'BTC': 10, 'ETH': 20, 'XRP': 70}
        investment = 1000000.0
        expected = {'BTC': 0.5, 'ETH': 1.0, 'XRP': 100.0}
        self.assertEqual(rebalance(krypfolio, prices, alloc, investment), expected)

    def test_rebalance_with_investment(self):
        krypfolio = {'BTC': 0.5, 'ETH': 1.0, 'XRP': 100.0}
        prices = {'BTC': 40000, 'ETH': 3000, 'XRP': 1.5}
        alloc = {'BTC': 10, 'ETH': 20, 'XRP': 70}
        investment = 500000.0
        expected = {'BTC': 0.25, 'ETH': 0.5, 'XRP': 50.0}
        self.assertEqual(rebalance(krypfolio, prices, alloc, investment), expected)

    def test_rebalance_with_no_investment(self):
        krypfolio = {'BTC': 0.5, 'ETH': 1.0, 'XRP': 100.0}
        prices = {'BTC': 40000, 'ETH': 3000, 'XRP': 1.5}
        alloc = {'BTC': 10, 'ETH': 20, 'XRP': 70}
        investment = 0.0
        expected = {'BTC': 0.5, 'ETH': 1.0, 'XRP': 100.0}
        self.assertEqual(rebalance(krypfolio, prices, alloc, investment), expected)

    def test_rebalance_with_different_allocations(self):
        krypfolio = {'BTC': 0.5, 'ETH': 1.0, 'XRP': 100.0}
        prices = {'BTC': 40000, 'ETH': 3000, 'XRP': 1.5}
        alloc = {'BTC': 20, 'ETH': 30, 'XRP': 50}
        investment = 1000000.0
        expected = {'BTC': 0.2, 'ETH': 0.3, 'XRP': 5.0}
        self.assertEqual(rebalance(krypfolio, prices, alloc, investment), expected)

if __name__ == '__main__':
    unittest.main()