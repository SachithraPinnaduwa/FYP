from subject_60 import *

import unittest

class TestBinarySearch(unittest.TestCase):
    def test_normal_case_target_present(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_normal_case_target_not_present(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_edge_case_empty_array(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_edge_case_single_element_present(self):
        self.assertEqual(binary_search([1], 1), 0)

    def test_edge_case_single_element_not_present(self):
        self.assertEqual(binary_search([1], 2), -1)

    def test_error_handling_non_sorted_array(self):
        self.assertEqual(binary_search([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 5), 4)

if __name__ == '__main__':
    unittest.main()