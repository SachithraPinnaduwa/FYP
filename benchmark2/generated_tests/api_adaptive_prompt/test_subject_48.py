from subject_48 import *

import unittest

class TestMergeSort(unittest.TestCase):
    def test_merge_sort_normal_case_unique_elements(self):
        arr = [5, 2, 9, 1, 5, 6]
        expected = [9, 6, 5, 5, 2, 1]
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, expected)
        self.assertEqual(swaps, 4)

    def test_merge_sort_normal_case_duplicate_elements(self):
        arr = [5, 2, 9, 1, 5, 6, 5]
        expected = [9, 6, 5, 5, 5, 2, 1]
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, expected)
        self.assertEqual(swaps, 4)

    def test_merge_sort_edge_case_empty_array(self):
        arr = []
        expected = []
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, expected)
        self.assertEqual(swaps, 0)

    def test_merge_sort_edge_case_single_element(self):
        arr = [4]
        expected = [4]
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, expected)
        self.assertEqual(swaps, 0)

    def test_merge_sort_edge_case_all_elements_same(self):
        arr = [3, 3, 3, 3]
        expected = [3, 3, 3, 3]
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, expected)
        self.assertEqual(swaps, 0)

    def test_merge_sort_error_handling_non_list_input(self):
        with self.assertRaises(TypeError):
            merge_sort(5)

    def test_merge_sort_error_handling_non_integer_elements(self):
        with self.assertRaises(TypeError):
            merge_sort([5, '2', 9, 1])

if __name__ == '__main__':
    unittest.main()