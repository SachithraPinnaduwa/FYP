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
    def test_binary_search_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([10, 20, 30, 40, 50], 30), 2)
        self.assertEqual(binary_search([0, 1, 2, 3, 4, 5], 4), 4)

    def test_binary_search_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(binary_search([10, 20, 30, 40, 50], 25), -1)
        self.assertEqual(binary_search([0, 1, 2, 3, 4, 5], -1), -1)

    def test_binary_search_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_binary_search_single_element(self):
        self.assertEqual(binary_search([1], 1), 0)
        self.assertEqual(binary_search([1], 2), -1)

if __name__ == '__main__':
    unittest.main()