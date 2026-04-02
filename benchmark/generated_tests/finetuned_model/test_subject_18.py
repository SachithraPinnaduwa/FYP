import unittest

class TestCalculateMedian(unittest.TestCase):
    def test_calculate_median_odd_length(self):
        self.assertEqual(calculate_median([7, 3, 5, 1]), 5)
        self.assertEqual(calculate_median([1, 3, 3, 6, 7, 8, 9]), 6)
        self.assertEqual(calculate_median([1, 2, 3, 4, 5, 6, 8, 9]), 4)
        self.assertEqual(calculate_median([1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)
        self.assertEqual(calculate_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5.5)

    def test_calculate_median_single_element(self):
        self.assertEqual(calculate_median([7]), 7)

    def test_calculate_median_two_elements(self):
        self.assertEqual(calculate_median([3, 1]), 2)

    def test_calculate_median_large_array(self):
        arr = list(range(1, 1000000))
        self.assertEqual(calculate_median(arr), 500000)

    def test_calculate_median_empty_array(self):
        with self.assertRaises(ValueError):
            calculate_median([])

if __name__ == '__main__':
    unittest.main()