from subject_69 import *

import unittest

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

class TestBinarySearch(unittest.TestCase):
    def test_normal_case_target_exists(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_normal_case_target_does_not_exist(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_edge_case_empty_array(self):
        self.assertEqual(binary_search([], 3), -1)

    def test_edge_case_single_element_match(self):
        self.assertEqual(binary_search([3], 3), 0)

    def test_edge_case_single_element_no_match(self):
        self.assertEqual(binary_search([3], 2), -1)

    def test_edge_case_duplicate_elements_target_exists(self):
        self.assertEqual(binary_search([1, 2, 2, 3, 4, 5], 2), 1)

    def test_error_handling_non_integer_target(self):
        with self.assertRaises(TypeError):
            binary_search([1, 2, 3, 4, 5], '3')

    def test_error_handling_non_integer_target_float(self):
        with self.assertRaises(TypeError):
            binary_search([1, 2, 3, 4, 5], 3.0)

    def test_error_handling_unsorted_array(self):
        with self.assertRaises(ValueError):
            binary_search([3, 1, 2, 4, 5], 2)

if __name__ == '__main__':
    unittest.main()