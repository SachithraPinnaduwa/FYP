from subject_29 import *

import unittest

def detect_even_odd(number):
    if not isinstance(number, int) or number <= 0 or number > 1000:
        return "Invalid Input"
    elif number % 2 == 0:
        return "Even"
    else:
        return "Odd"

class TestDetectEvenOdd(unittest.TestCase):
    def test_normal_case_even_number(self):
        self.assertEqual(detect_even_odd(200), "Even")

    def test_normal_case_odd_number(self):
        self.assertEqual(detect_even_odd(301), "Odd")

    def test_edge_case_lower_boundary(self):
        self.assertEqual(detect_even_odd(1), "Odd")

    def test_edge_case_upper_boundary(self):
        self.assertEqual(detect_even_odd(1000), "Even")

    def test_error_handling_outside_range(self):
        self.assertEqual(detect_even_odd(1001), "Invalid Input")

    def test_error_handling_non_integer(self):
        self.assertEqual(detect_even_odd(3.14), "Invalid Input")

    def test_error_handling_negative_number(self):
        self.assertEqual(detect_even_odd(-50), "Invalid Input")

if __name__ == '__main__':
    unittest.main()