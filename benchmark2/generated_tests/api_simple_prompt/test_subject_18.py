from subject_18 import *

import unittest

def calculate_median(arr):
    n = len(arr)
    middle_index = (n - 1) // 2
    median = arr[middle_index]
    return median

class TestCalculateMedian(unittest.TestCase):
    def test_calculate_median_odd_length(self):
        self.assertEqual(calculate_median([3, 1, 2, 4, 5]), 3)
        self.assertEqual(calculate_median([-10, 4, 6, 1000, 10, 20]), 15)
        self.assertEqual(calculate_median([1, 2, 3, 4, 5, 6, 7]), 4)

    def test_calculate_median_single_element(self):
        self.assertEqual(calculate_median([7]), 7)

    def test_calculate_median_even_length(self):
        with self.assertRaises(ValueError):
            calculate_median([1, 2, 3, 4])

    def test_calculate_median_empty_array(self):
        with self.assertRaises(ValueError):
            calculate_median([])

if __name__ == '__main__':
    unittest.main()