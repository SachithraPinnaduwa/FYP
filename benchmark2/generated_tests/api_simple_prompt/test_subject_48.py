from subject_48 import *

import unittest

class TestMergeSort(unittest.TestCase):
    def test_merge_sort_empty_array(self):
        self.assertEqual(merge_sort([]), ([], 0))

    def test_merge_sort_single_element(self):
        self.assertEqual(merge_sort([5]), ([5], 0))

    def test_merge_sort_two_elements(self):
        self.assertEqual(merge_sort([3, 1]), ([3, 1], 1))

    def test_merge_sort_multiple_elements(self):
        self.assertEqual(merge_sort([4, 1, 3, 2]), ([4, 3, 2, 1], 5))

    def test_merge_sort_with_duplicates(self):
        self.assertEqual(merge_sort([4, 1, 3, 2, 4]), ([4, 4, 3, 2, 1], 6))

    def test_merge_sort_descending_order(self):
        self.assertEqual(merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0))

    def test_merge_sort_random_order(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), ([9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1], 20))

if __name__ == '__main__':
    unittest.main()