from subject_21 import *

import unittest

class TestGreedySumSubset(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(greedy_sum_subset([10, 20, 30, 40, 50], 100), [[10, 20, 30, 40], [50]])

    def test_edge_case_empty_array(self):
        self.assertEqual(greedy_sum_subset([], 100), [[]])

    def test_edge_case_all_elements_greater_than_target_sum(self):
        self.assertEqual(greedy_sum_subset([100, 200, 300], 50), [[100], [200], [300]])

    def test_error_handling_negative_numbers(self):
        self.assertEqual(greedy_sum_subset([-10, 20, -30, 40, 50], 100), [[20, 40, 50], [-10, -30]])

    def test_error_handling_zero(self):
        self.assertEqual(greedy_sum_subset([0, 20, 30, 40, 50], 100), [[20, 30, 40, 50], [0]])

if __name__ == '__main__':
    unittest.main()