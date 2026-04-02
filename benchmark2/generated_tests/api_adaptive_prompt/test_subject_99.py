from subject_99 import *

import unittest

class TestSumEven(unittest.TestCase):
    def test_normal_case_single_even_number(self):
        self.assertEqual(sum_even([10]), 10)

    def test_normal_case_single_odd_number(self):
        self.assertEqual(sum_even([11]), 0)

    def test_normal_case_empty_list(self):
        self.assertEqual(sum_even([]), 0)

    def test_normal_case_mixed_even_and_odd_numbers(self):
        self.assertEqual(sum_even([1, 2, 3, 4, 5]), 6)

    def test_normal_case_list_of_even_numbers(self):
        self.assertEqual(sum_even([2, 4, 6, 8]), 20)

    def test_edge_case_maximum_integer_value(self):
        self.assertEqual(sum_even([2147483647]), 0)

    def test_edge_case_minimum_integer_value(self):
        self.assertEqual(sum_even([-2147483648]), 0)

    def test_error_handling_non_integer_element(self):
        self.assertEqual(sum_even([1, '2', 3]), 0)

    def test_error_handling_none_value(self):
        self.assertEqual(sum_even([1, None, 3]), 0)

if __name__ == '__main__':
    unittest.main()