from subject_18 import *

import unittest

def calculate_median(arr):
    n = len(arr)
    middle_index = (n - 1) // 2
    median = arr[middle_index]
    return median

class TestCalculateMedian(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(calculate_median([1, 3, 2]), 2)

    def test_edge_case_single_element(self):
        self.assertEqual(calculate_median([7]), 7)

    def test_edge_case_smallest_value(self):
        self.assertEqual(calculate_median([-1000000000]), -1000000000)

    def test_edge_case_largest_value(self):
        self.assertEqual(calculate_median([1000000000]), 1000000000)

    def test_error_handling_empty_array(self):
        with self.assertRaises(ValueError):
            calculate_median([])

if __name__ == '__main__':
    unittest.main()