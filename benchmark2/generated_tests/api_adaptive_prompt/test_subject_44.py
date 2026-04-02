from subject_44 import *

import unittest

def find_k_for_digit_power_sum(n, p):
    s = 0
    for i, c in enumerate(str(n)):
        s += pow(int(c), p + i)
    return s // n if s % n == 0 else -1

class TestFindKForDigitPowerSum(unittest.TestCase):
    def test_normal_case_with_valid_k_value(self):
        self.assertEqual(find_k_for_digit_power_sum(89, 1), 1)
        self.assertEqual(find_k_for_digit_power_sum(695, 2), 2)
        self.assertEqual(find_k_for_digit_power_sum(46288, 3), 51)

    def test_normal_case_with_invalid_k_value(self):
        self.assertEqual(find_k_for_digit_power_sum(92, 1), -1)

    def test_edge_case_with_smallest_possible_values(self):
        self.assertEqual(find_k_for_digit_power_sum(10, 1), -1)

    def test_error_handling_with_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            find_k_for_digit_power_sum('abc', 1)
        with self.assertRaises(TypeError):
            find_k_for_digit_power_sum(10, 'abc')

if __name__ == '__main__':
    unittest.main()