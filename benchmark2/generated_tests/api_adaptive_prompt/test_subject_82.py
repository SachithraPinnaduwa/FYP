from subject_82 import *

import unittest

def polynomial(x, a, b, c, d, e):
    """
    Calculate the result of a polynomial equation of degree 4.

    Parameters:
    x (float): The value of x in the equation.
    a (float): The coefficient of x⁴.
    b (float): The coefficient of x³.
    c (float): The coefficient of x².
    d (float): The coefficient of x.
    e (float): The constant term.

    Returns:
    float: The result of the polynomial equation.
    """
    return a * x**4 + b * x**3 + c * x**2 + d * x + e

class TestPolynomial(unittest.TestCase):
    def test_normal_case_positive_coefficients(self):
        self.assertEqual(polynomial(2, 1, 2, 3, 4, 5), 57)

    def test_normal_case_negative_coefficients(self):
        self.assertEqual(polynomial(-1, -1, -2, -3, -4, -5), -3)

    def test_normal_case_zero_coefficient(self):
        self.assertEqual(polynomial(3, 0, 1, 0, 2, 0), 33)

    def test_edge_case_zero_x(self):
        self.assertEqual(polynomial(0, 1, 2, 3, 4, 5), 5)

    def test_edge_case_large_x(self):
        self.assertEqual(polynomial(1000000, 1, 0, 0, 0, 0), 1000000000000000000000000000000)

    def test_error_handling_non_number_x(self):
        with self.assertRaises(ValueError) as context:
            polynomial('a', 1, 2, 3, 4, 5)
        self.assertEqual(str(context.exception), 'x must be a number.')

    def test_error_handling_non_number_coefficients(self):
        with self.assertRaises(ValueError) as context:
            polynomial(2, 'a', 2, 3, 4, 5)
        self.assertEqual(str(context.exception), 'Coefficients a, b, c, d, and e must be numbers.')

if __name__ == '__main__':
    unittest.main()