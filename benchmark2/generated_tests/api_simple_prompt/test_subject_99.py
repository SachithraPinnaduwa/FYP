from subject_99 import *

import unittest

class TestSumEven(unittest.TestCase):
    def test_sum_even_empty_list(self):
        self.assertEqual(sum_even([]), 0)

    def test_sum_even_single_even_number(self):
        self.assertEqual(sum_even([2]), 2)

    def test_sum_even_single_odd_number(self):
        self.assertEqual(sum_even([1]), 0)

    def test_sum_even_mixed_numbers(self):
        self.assertEqual(sum_even([1, 2, 3, 4, 5, 6]), 12)

    def test_sum_even_all_even_numbers(self):
        self.assertEqual(sum_even([2, 4, 6, 8]), 20)

    def test_sum_even_all_odd_numbers(self):
        self.assertEqual(sum_even([1, 3, 5, 7]), 0)

    def test_sum_even_nested_lists(self):
        self.assertEqual(sum_even([1, [2, 3], 4, [5, [6, 7]]]), 12)

if __name__ == '__main__':
    unittest.main()