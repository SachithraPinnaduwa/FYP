from subject_67 import *

import unittest

class TestComputeSum(unittest.TestCase):
    def test_normal_case_sum_divisible_by_divisor(self):
        self.assertEqual(compute_sum([10, 20, 30], 5), 60.00)

    def test_normal_case_sum_not_divisible_by_divisor(self):
        self.assertEqual(compute_sum([10, 20, 30], 3), 61)

    def test_edge_case_empty_list(self):
        self.assertEqual(compute_sum([], 5), 0.00)

    def test_edge_case_single_integer(self):
        self.assertEqual(compute_sum([5], 5), 5.00)

    def test_error_handling_divisor_zero(self):
        with self.assertRaises(ValueError) as context:
            compute_sum([10, 20, 30], 0)
        self.assertIn("math domain error", str(context.exception))

if __name__ == '__main__':
    unittest.main()