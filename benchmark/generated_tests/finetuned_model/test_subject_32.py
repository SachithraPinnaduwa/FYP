import unittest

class TestMinCoins(unittest.TestCase):
    def test_minCoins(self):
        self.assertEqual(minCoins([1, 2, 3], 4), 2)
        self.assertEqual(minCoins([1, 2, 5], 11), 3)
        self.assertEqual(minCoins([1, 5, 10, 25], 30), 2)
        self.assertEqual(minCoins([1, 3, 4, 5], 7), 2)
        self.assertEqual(minCoins([2, 5, 10, 25], 3), -1)
        self.assertEqual(minCoins([1], 0), 0)
        self.assertEqual(minCoins([1], 1), 1)
        self.assertEqual(minCoins([1, 1, 1, 1], 10), 10)

if __name__ == '__main__':
    unittest.main()