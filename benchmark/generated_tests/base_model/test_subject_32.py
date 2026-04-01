import unittest

class TestMinCoins(unittest.TestCase):

    def test_minCoins(self):
        self.assertEqual(minCoins([1, 2, 5], 11), 3)
        self.assertEqual(minCoins([1, 2, 5], 4), 2)
        self.assertEqual(minCoins([2, 3, 7], 7), 1)
        self.assertEqual(minCoins([2, 3, 7], 6), 2)
        self.assertEqual(minCoins([1, 2, 5], 0), 0)
        self.assertEqual(minCoins([1, 2, 5], 1), 1)
        self.assertEqual(minCoins([1, 2, 5], 18), 4)
        self.assertEqual(minCoins([3, 9, 12], 18), 2)
        self.assertEqual(minCoins([1, 5, 10, 25], 30), 2)
        self.assertEqual(minCoins([1, 5, 10, 25], 31), -1)

if __name__ == '__main__':
    unittest.main()