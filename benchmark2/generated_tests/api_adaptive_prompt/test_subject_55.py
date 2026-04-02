from subject_55 import *

import unittest

def smallest_positive_no_compare(lst: list):
    """Return the least positive number in dataset lst without the use of comparative functions.
    Handles both negative and positive numbers within datasets."""
    smallest = float('inf')
    for i in lst:
        if i <= 0:
            continue
        if smallest - i > 0:
            smallest = i
    return smallest if smallest != float('inf') else None

class TestSmallestPositiveNoCompare(unittest.TestCase):
    def test_normal_case_with_negative_and_positive_numbers(self):
        self.assertEqual(smallest_positive_no_compare([-3, -1, 0, 2, 5]), 2)

    def test_normal_case_with_only_negative_numbers(self):
        self.assertIsNone(smallest_positive_no_compare([-10, -20, -30]))

    def test_normal_case_with_only_positive_numbers(self):
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4]), 1)

    def test_normal_case_with_empty_list(self):
        self.assertIsNone(smallest_positive_no_compare([]))

    def test_edge_case_with_single_positive_number(self):
        self.assertEqual(smallest_positive_no_compare([7]), 7)

    def test_edge_case_with_single_negative_number(self):
        self.assertIsNone(smallest_positive_no_compare([-7]))

    def test_edge_case_with_single_zero(self):
        self.assertIsNone(smallest_positive_no_compare([0]))

    def test_error_handling_with_non_list_input(self):
        with self.assertRaises(TypeError):
            smallest_positive_no_compare(5)

    def test_error_handling_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            smallest_positive_no_compare([1, 'two', 3])

if __name__ == '__main__':
    unittest.main()