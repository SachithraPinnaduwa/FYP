from subject_32 import *

import unittest

class TestMinCoins(unittest.TestCase):
    def test_minCoins(self):
        self.assertEqual(minCoins([1, 2, 5], 11), 3)
        self.assertEqual(minCoins([2, 5, 10, 1], 12), 3)
        self.assertEqual(minCoins([1, 2, 3], 6), 2)
        self.assertEqual(minCoins([1, 2, 5], 100), 20)
        self.assertEqual(minCoins([1, 2, 5], 0), 0)
        self.assertEqual(minCoins([10, 20, 50], 37), -1)

if __name__ == '__main__':
    unittest.main()