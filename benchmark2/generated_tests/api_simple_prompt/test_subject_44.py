from subject_44 import *

import unittest

def find_k_for_digit_power_sum(n, p):
    s = 0
    for i, c in enumerate(str(n)):
        s += pow(int(c), p + i)
    return s // n if s % n == 0 else -1

class TestFindKForDigitPowerSum(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(find_k_for_digit_power_sum(89, 1), 1)
        self.assertEqual(find_k_for_digit_power_sum(92, 1), -1)
        self.assertEqual(find_k_for_digit_power_sum(695, 2), 2)
        self.assertEqual(find_k_for_digit_power_sum(46288, 3), 51)
        self.assertEqual(find_k_for_digit_power_sum(11, 5), 1)
        self.assertEqual(find_k_for_digit_power_sum(89, 2), -1)
        self.assertEqual(find_k_for_digit_power_sum(92, 2), -1)
        self.assertEqual(find_k_for_digit_power_sum(695, 3), -1)
        self.assertEqual(find_k_for_digit_power_sum(46288, 4), -1)

if __name__ == '__main__':
    unittest.main()