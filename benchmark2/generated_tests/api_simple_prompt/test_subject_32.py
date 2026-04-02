from subject_32 import *

import unittest

class TestMinCoins(unittest.TestCase):
    def test_minCoins(self):
        self.assertEqual(minCoins([1, 2, 5], 11), 3)
        self.assertEqual(minCoins([2, 5, 10], 12), 3)
        self.assertEqual(minCoins([1, 3, 4, 5], 7), 2)
        self.assertEqual(minCoins([1, 2, 3], 6), 2)
        self.assertEqual(minCoins([1, 2, 3], 1), 1)
        self.assertEqual(minCoins([1, 2, 3], 0), 0)
        self.assertEqual(minCoins([1, 2, 3], 100), -1)
        self.assertEqual(minCoins([10, 20, 30], 10), 1)
        self.assertEqual(minCoins([10, 20, 30], 20), 1)
        self.assertEqual(minCoins([10, 20, 30], 30), 1)
        self.assertEqual(minCoins([10, 20, 30], 40), 2)
        self.assertEqual(minCoins([10, 20, 30], 50), 2)
        self.assertEqual(minCoins([10, 20, 30], 60), 2)
        self.assertEqual(minCoins([10, 20, 30], 70), 3)
        self.assertEqual(minCoins([10, 20, 30], 80), 3)
        self.assertEqual(minCoins([10, 20, 30], 90), 3)
        self.assertEqual(minCoins([10, 20, 30], 100), 4)

if __name__ == '__main__':
    unittest.main()