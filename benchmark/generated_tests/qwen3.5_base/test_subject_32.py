import unittest

class TestMinCoins(unittest.TestCase):
    def test_minCoins(self):
        # Test case 1
        coins = [1, 2, 5]
        N = 11
        self.assertEqual(minCoins(coins, N), 3)
        
        # Test case 2
        coins = [1, 3, 4]
        N = 12
        self.assertEqual(minCoins(coins, N), 5)
        
        # Test case 3
        coins = [1, 2, 3]
        N = 10
        self.assertEqual(minCoins(coins, N), 4)
        
        # Test case 4
        coins = [1, 2, 3]
        N = 100
        self.assertEqual(minCoins(coins, N), 50)
        
        # Test case 5
        coins = [1, 2, 3]
        N = 1000
        self.assertEqual(minCoins(coins, N), 500)
        
        # Test case 6
        coins = [1, 2, 3]
        N = 10000
        self.assertEqual(minCoins(coins, N), 5000)
        
        # Test case 7
        coins = [1, 2, 3]
        N = 100000
        self.assertEqual(minCoins(coins, N), 50000)
        
        # Test case 8
        coins = [1, 2, 3]
        N = 1000000
        self.assertEqual(minCoins(coins, N), 500000)
        
        # Test case 9
        coins = [1, 2, 3]
        N = 10000000
        self.assertEqual(minCoins(coins, N), 5000000)
        
        # Test case 10
        coins = [1, 2, 3]
        N = 100000000
        self.assertEqual(minCoins(coins, N), 50000000)
        
        # Test case 11
        coins = [1, 2, 3]
        N = 1000000000
        self.assertEqual(minCoins(coins, N), 500000000)
        
        # Test case 12
        coins = [1, 2, 3]
        N = 10000000000
        self.assertEqual(minCoins(coins, N), 5000000000)
        
        # Test case 13
        coins = [1, 2, 3]
        N = 100000000000
        self.assertEqual(minCoins(coins, N), 50000000000)
        
        # Test case 14
        coins = [1, 2, 3]
        N = 1000000000000
        self.assertEqual(minCoins(coins, N), 500000000000)
        
        # Test case 15
        coins = [1, 2, 3]
        N = 10000000000000
        self.assertEqual(minCoins(coins, N), 5000000000000)
        
        # Test case 16
        coins = [1, 2, 3]
        N = 100000000000000
        self.assertEqual(minCoins(coins, N), 50000000000000)
        
        # Test case 17
        coins = [1, 2, 3]
        N = 1000000000000000
        self.assertEqual(minCoins(coins, N), 500000000000000)
        
        # Test case 18
        coins = [1, 2, 3]
        N = 10000000000000000
        self.assertEqual(minCoins(coins, N), 5000000000000000)
        
        # Test case 19
        coins = [1, 2, 3]
        N = 100000000000000000
        self.assertEqual(minCoins(coins, N), 50000000000000000)
        
        # Test case 20
        coins = [1, 2, 3]
        N = 1000000000000000000
        self.assertEqual(minCoins(coins, N), 500000000000000000)
        
        # Test case 21
        coins = [1, 2, 3]
        N = 10000000000000000000
        self.assertEqual(minCoins(coins, N), 5000000000000000000)
        
        # Test case 22
        coins = [1, 2, 3]
        N = 100000000000000000000
        self.assertEqual(minCoins(coins, N), 50000000000000000000)
        
        # Test case 23
        coins = [1, 2, 3]
        N = 1000000000000000000000
        self.assertEqual(minCoins(coins, N), 500000000000000000000)
        
        # Test case 24
        coins = [1, 2, 3]
        N = 10000000000000000000000
        self.assertEqual(minCoins(coins, N), 5000000000000000000000)
        
        # Test case 25
        coins = [1, 2, 3]
        N = 1000000000