from subject_40 import *

import unittest

def min_increment_operations(arr, N):
    c = 0
    arr.sort()
    for i in range(1, N):
        if arr[i] <= arr[i - 1]:
            c += arr[i - 1] + 1 - arr[i]
            arr[i] = arr[i - 1] + 1
    return c

class TestMinIncrementOperations(unittest.TestCase):
    def test_normal_case_1(self):
        self.assertEqual(min_increment_operations([1, 2, 2], 3), 1)

    def test_normal_case_2(self):
        self.assertEqual(min_increment_operations([1, 1, 2, 3], 4), 3)

    def test_edge_case_unique_elements(self):
        self.assertEqual(min_increment_operations([1, 2, 3, 4], 4), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(min_increment_operations([5], 1), 0)

    def test_error_handling_negative_number(self):
        with self.assertRaises(ValueError):
            min_increment_operations([-1, 2, 3], 3)

    def test_error_handling_empty_array(self):
        with self.assertRaises(ValueError):
            min_increment_operations([], 0)

if __name__ == '__main__':
    unittest.main()