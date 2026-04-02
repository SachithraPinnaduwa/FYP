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
    def test_empty_list(self):
        self.assertEqual(sum_list_recursive([]), 0)

    def test_single_element_list(self):
        self.assertEqual(sum_list_recursive([5]), 5)

    def test_multiple_elements_list(self):
        self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers(self):
        self.assertEqual(sum_list_recursive([-1, -2, -3, -4, -5]), -15)

    def test_mixed_numbers(self):
        self.assertEqual(sum_list_recursive([1, -2, 3, -4, 5]), 3)

    def test_large_list(self):
        large_list = list(range(1, 1001))
        self.assertEqual(sum_list_recursive(large_list), sum(large_list))

if __name__ == '__main__':
    unittest.main()