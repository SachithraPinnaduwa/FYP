from subject_62 import *

import unittest

def cubic_product(a, b, c):
    return (a**3) * (b**3) * (c**3)

class TestCubicProduct(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(cubic_product(2, 3, 4), 27648)

    def test_negative_numbers(self):
        self.assertEqual(cubic_product(-1, -2, -3), -216)

    def test_mixed_numbers(self):
        self.assertEqual(cubic_product(1, -2, 3), -216)

    def test_zero(self):
        self.assertEqual(cubic_product(0, 0, 0), 0)

    def test_float_numbers(self):
        self.assertAlmostEqual(cubic_product(1.5, 2.5, 3.5), 1234.375)

if __name__ == '__main__':
    unittest.main()