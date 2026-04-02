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
    def test_polynomial(self):
        self.assertEqual(polynomial(1, 1, 0, 0, 0, 0), 1)
        self.assertEqual(polynomial(2, 1, 0, 0, 0, 0), 16)
        self.assertEqual(polynomial(3, 1, 0, 0, 0, 0), 81)
        self.assertEqual(polynomial(0, 1, 0, 0, 0, 0), 0)
        self.assertEqual(polynomial(1, 0, 1, 0, 0, 0), 1)
        self.assertEqual(polynomial(1, 0, 0, 1, 0, 0), 1)
        self.assertEqual(polynomial(1, 0, 0, 0, 1, 0), 1)
        self.assertEqual(polynomial(1, 0, 0, 0, 0, 1), 1)
        self.assertEqual(polynomial(1, 1, 1, 1, 1, 1), 5)
        self.assertEqual(polynomial(-1, 1, 1, 1, 1, 1), 1)
        self.assertEqual(polynomial(2, 1, 1, 1, 1, 1), 35)
        self.assertEqual(polynomial(-2, 1, 1, 1, 1, 1), -35)
        self.assertEqual(polynomial(1, 1, -1, 1, -1, 1), 1)
        self.assertEqual(polynomial(2, 1, -1, 1, -1, 1), 15)
        self.assertEqual(polynomial(-2, 1, -1, 1, -1, 1), -15)

if __name__ == '__main__':
    unittest.main()