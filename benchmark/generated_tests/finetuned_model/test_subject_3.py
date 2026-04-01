import unittest

class TestFactorialFunction(unittest.TestCase):
    def test_base_case_zero(self):
        # Test the base case for factorial(0)
        self.assertEqual(factorial_(0), 1)

    def test_base_case_one(self):
        # Test the base case for factorial(1)
        self.assertEqual(factorial_(1), 1)

    def test_factorial_of_two(self):
        # Test the factorial of a number greater than 1
        self.assertEqual(factorial_(2), 2)

    def test_factorial_of_three(self):
        # Test the factorial of a number greater than 1
        self.assertEqual(factorial_(3), 6)

    def test_factorial_of_five(self):
        # Test the factorial of a number greater than 1
        self.assertEqual(factorial_(5), 120)

    def test_factorial_of_ten(self):
        # Test the factorial of a number greater than 1
        self.assertEqual(factorial_(10), 3628800)