from subject_67 import *

import unittest

def compute_sum(x, K):
    total = sum(x)

    if total % K == 0:
        return format(total, ".2f")
    else:
        return math.ceil(total)

class TestComputeSum(unittest.TestCase):
    def test_divisible_by_K(self):
        self.assertEqual(compute_sum([10, 20, 30], 10), "60.00")

    def test_not_divisible_by_K(self):
        self.assertEqual(compute_sum([10, 20, 30], 7), 61)

    def test_single_element_divisible_by_K(self):
        self.assertEqual(compute_sum([20], 20), "20.00")

    def test_single_element_not_divisible_by_K(self):
        self.assertEqual(compute_sum([20], 7), 21)

    def test_empty_list(self):
        self.assertEqual(compute_sum([], 10), 0)

    def test_large_numbers(self):
        self.assertEqual(compute_sum([1000000, 2000000], 3000000), 3000000.00)

    def test_negative_numbers(self):
        self.assertEqual(compute_sum([-10, -20, -30], 10), "-60.00")

    def test_mixed_numbers(self):
        self.assertEqual(compute_sum([10, -20, 30], 10), "10.00")

if __name__ == '__main__':
    unittest.main()