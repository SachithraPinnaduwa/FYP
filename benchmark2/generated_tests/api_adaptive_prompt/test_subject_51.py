from subject_51 import *

import unittest

def sum_list_recursive(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_list_recursive(lst[1:])

class TestSumListRecursive(unittest.TestCase):
    def test_sum_list_recursive_normal_case_multiple_elements(self):
        self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5]), 15)

    def test_sum_list_recursive_normal_case_single_element(self):
        self.assertEqual(sum_list_recursive([10]), 10)

    def test_sum_list_recursive_normal_case_empty_list(self):
        self.assertEqual(sum_list_recursive([]), 0)

    def test_sum_list_recursive_edge_case_negative_numbers(self):
        self.assertEqual(sum_list_recursive([-1, -2, -3, -4, -5]), -15)

    def test_sum_list_recursive_edge_case_mixed_numbers(self):
        self.assertEqual(sum_list_recursive([1, -2, 3, -4, 5]), 3)

    def test_sum_list_recursive_error_handling_non_list_input(self):
        with self.assertRaises(TypeError):
            sum_list_recursive('string')

if __name__ == '__main__':
    unittest.main()