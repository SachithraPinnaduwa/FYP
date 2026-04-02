import unittest

class TestMedian(unittest.TestCase):
    def test_calculate_median(self):
        self.assertEqual(calculate_median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calculate_median([1, 2, 3, 4, 5, 6]), 3.5)
        self.assertEqual(calculate_median([1, 2, 3, 4, 5, 6, 7]), 4)
        self.assertEqual(calculate_median([1, 2, 3, 4, 5, 6, 7, 8]), 4.5)
        self.assertEqual(calculate_median([1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)

if __name__ == '__main__':
    unittest.main()