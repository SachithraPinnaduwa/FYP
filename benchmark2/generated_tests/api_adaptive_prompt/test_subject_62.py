from subject_62 import *

import unittest

def cubic_product(a, b, c):
    return (a**3) * (b**3) * (c**3)

class TestCubicProduct(unittest.TestCase):
    def test_normal_case_positive_integers(self):
        self.assertEqual(cubic_product(2, 3, 4), 216)

    def test_normal_case_negative_integers(self):
        self.assertEqual(cubic_product(-2, -3, -4), -216)

    def test_normal_case_zero(self):
        self.assertEqual(cubic_product(0, 0, 0), 0)

    def test_normal_case_floating_point_numbers(self):
        self.assertAlmostEqual(cubic_product(1.5, 2.5, 3.5), 1295.0625)

    def test_normal_case_mixed_integers(self):
        self.assertEqual(cubic_product(1, -2, 3), -27)

    def test_error_handling_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            cubic_product('a', 'b', 'c')

    def test_error_handling_none_as_input(self):
        with self.assertRaises(TypeError):
            cubic_product(None, None, None)

if __name__ == '__main__':
    unittest.main()