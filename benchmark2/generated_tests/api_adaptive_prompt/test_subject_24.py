from subject_24 import *

import unittest

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

class TestBinarySearch(unittest.TestCase):
    def test_normal_case_element_exists(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5), 4)

    def test_normal_case_element_does_not_exist(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10), -1)

    def test_edge_case_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_edge_case_single_element_list(self):
        self.assertEqual(binary_search([1], 1), 0)

    def test_error_handling_non_sorted_list(self):
        self.assertEqual(binary_search([3, 1, 4, 1, 5, 9, 2, 6, 5], 5), 4)

    def test_error_handling_non_integer_values(self):
        self.assertEqual(binary_search([1, '2', 3, 4.0], '2'), -1)

if __name__ == '__main__':
    unittest.main()