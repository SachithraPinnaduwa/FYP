import unittest

class TestRebalance(unittest.TestCase):
    def test_rebalance(self):
        krypfolio = {'BTC': 0.5, 'ETH': 1.0}
        prices = {'BTC': 50000, 'ETH': 3000}
        alloc = {'BTC': 50, 'ETH': 50}
        investment = 10000
        
        expected_krypfolio = {'BTC': 1.0, 'ETH': 1.0}
        expected_investment = 0
        
        result = rebalance(krypfolio, prices, alloc, investment)
        
        self.assertEqual(result, expected_krypfolio)
        self.assertEqual(investment, expected_investment)

if __name__ == '__main__':
    unittest.main()
