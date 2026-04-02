from subject_60 import *

import unittest

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1

class TestBinarySearch(unittest.TestCase):
    def test_binary_search_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 4), 3)
        self.assertEqual(binary_search([10, 20, 30, 40, 50], 30), 2)
        self.assertEqual(binary_search([100, 200, 300, 400, 500], 500), 4)

    def test_binary_search_not_found(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 2), -1)
        self.assertEqual(binary_search([10, 20, 30, 40], 25), -1)
        self.assertEqual(binary_search([100, 200, 300, 400, 500], 600), -1)

    def test_binary_search_empty_array(self):
        self.assertEqual(binary_search([], 5), -1)

    def test_binary_search_single_element(self):
        self.assertEqual(binary_search([5], 5), 0)
        self.assertEqual(binary_search([10], 20), -1)

if __name__ == '__main__':
    unittest.main()