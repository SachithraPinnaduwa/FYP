import unittest

class TestSumEven(unittest.TestCase):
    def test_sum_even(self):
        self.assertEqual(sum_even([1, 2, 3, 4, 5]), 6)
        self.assertEqual(sum_even([1, 3, 5]), 0)
        self.assertEqual(sum_even([]), 0)

if __name__ == '__main__':
    unittest.main()