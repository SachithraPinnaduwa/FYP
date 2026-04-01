import unittest

class TestRebalance(unittest.TestCase):

    def setUp(self):
        self.krypfolio = {'BTC': 2.5, 'ETH': 10.0, 'LTC': 5.0}
        self.prices = {'BTC': 30000.0, 'ETH': 2000.0, 'LTC': 200.0}
        self.alloc = {'BTC': 40, 'ETH': 40, 'LTC': 20}
        self.investment = 100000.0

    def test_rebalance_full_allocation(self):
        result = rebalance(self.krypfolio, self.prices, self.alloc, self.investment)
        expected = {
            'BTC': 40000.0,
            'ETH': 40000.0,
            'LTC': 20000.0
        }
        self.assertEqual(result, expected)

    def test_rebalance_under_allocated(self):
        self.alloc['BTC'] = 50
        self.alloc['ETH'] = 30
        self.alloc['LTC'] = 20
        result = rebalance(self.krypfolio, self.prices, self.alloc, self.investment)
        expected = {
            'BTC': 50000.0,
            'ETH': 30000.0,
            'LTC': 20000.0
        }
        self.assertEqual(result, expected)

    def test_rebalance_over_allocated(self):
        self.alloc['BTC'] = 30
        self.alloc['ETH'] = 30
        self.alloc['LTC'] = 40
        result = rebalance(self.krypfolio, self.prices, self.alloc, self.investment)
        expected = {
            'BTC': 30000.0,
            'ETH': 30000.0,
            'LTC': 40000.0
        }
        self.assertEqual(result, expected)

    def test_rebalance_no_changes(self):
        self.alloc['BTC'] = 25
        self.alloc['ETH'] = 25
        self.alloc['LTC'] = 50
        result = rebalance(self.krypfolio, self.prices, self.alloc, self.investment)
        expected = {
            'BTC': 25000.0,
            'ETH': 25000.0,
            'LTC': 50000.0
        }
        self.assertEqual(result, expected)

    def test_rebalance_with_zero_investment(self):
        result = rebalance(self.krypfolio, self.prices, self.alloc, 0.0)
        expected = {
            'BTC': 2.5,
            'ETH': 10.0,
            'LTC': 5.0
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()