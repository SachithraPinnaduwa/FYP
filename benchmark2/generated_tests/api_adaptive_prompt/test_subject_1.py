from subject_1 import *

import unittest

def median_in_interval(numbers, lower_limit, upper_limit):
    numbers.sort()
    if len(numbers) % 2 == 0:  # Even number of elements
        median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
    else:  # Odd number of elements
        median = numbers[len(numbers)//2]
    return lower_limit <= median <= upper_limit

class TestMedianInInterval(unittest.TestCase):
    def test_normal_case_odd_median_within_interval(self):
        self.assertTrue(median_in_interval([1, 3, 5], 2, 6))

    def test_normal_case_even_median_within_interval(self):
        self.assertTrue(median_in_interval([2, 4, 6, 8], 3, 7))

    def test_normal_case_odd_median_outside_interval(self):
        self.assertFalse(median_in_interval([1, 3, 5], 6, 10))

    def test_normal_case_even_median_outside_interval(self):
        self.assertFalse(median_in_interval([2, 4, 6, 8], 1, 3))

    def test_normal_case_odd_median_equals_lower_limit(self):
        self.assertTrue(median_in_interval([1, 3, 5], 1, 6))

    def test_normal_case_even_median_equals_lower_limit(self):
        self.assertTrue(median_in_interval([2, 4, 6, 8], 2, 7))

    def test_normal_case_odd_median_equals_upper_limit(self):
        self.assertTrue(median_in_interval([1, 3, 5], 2, 5))

    def test_normal_case_even_median_equals_upper_limit(self):
        self.assertTrue(median_in_interval([2, 4, 6, 8], 3, 8))

    def test_normal_case_odd_median_equals_both_limits(self):
        self.assertTrue(median_in_interval([5, 5, 5], 5, 5))

    def test_normal_case_even_median_equals_both_limits(self):
        self.assertTrue(median_in_interval([4, 4, 4, 4], 4, 4))

    def test_normal_case_empty_list(self):
        self.assertFalse(median_in_interval([], 0, 10))

if __name__ == '__main__':
    unittest.main()