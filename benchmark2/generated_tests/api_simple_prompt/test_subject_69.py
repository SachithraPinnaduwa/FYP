from subject_69 import *

import unittest

class TestBinarySearch(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(binary_search([], 5), -1)

    def test_single_element_array(self):
        self.assertEqual(binary_search([5], 5), 0)
        self.assertEqual(binary_search([5], 3), -1)

    def test_target_not_in_array(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0), -1)

    def test_target_at_start(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_target_at_end(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_target_in_middle(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_duplicate_elements(self):
        self.assertEqual(binary_search([1, 2, 2, 3, 4, 5], 2), 1)
        self.assertEqual(binary_search([1, 2, 2, 3, 4, 5], 4), 4)

    def test_target_at_first_duplicate(self):
        self.assertEqual(binary_search([1, 1, 2, 3, 4, 5], 1), 0)

    def test_target_at_last_duplicate(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 4, 4], 4), 4)

if __name__ == '__main__':
    unittest.main()