from subject_3 import *

import unittest

class TestFactorialFunction(unittest.TestCase):
    def test_normal_case_factorial_of_positive_integer(self):
        # Test the factorial of a positive integer
        self.assertEqual(factorial_(10), 3628800)

    def test_normal_case_factorial_of_zero(self):
        # Test the factorial of 0
        self.assertEqual(factorial_(0), 1)

    def test_edge_case_factorial_of_one(self):
        # Test the factorial of 1
        self.assertEqual(factorial_(1), 1)

    def test_error_handling_negative_input(self):
        # Test error handling for negative inputs
        self.assertIsNone(factorial_(-1))

if __name__ == '__main__':
    unittest.main()