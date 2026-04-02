from subject_43 import *

import unittest

def triangle_area(base, height):
    """
    Calculate the area of a triangle given its base and height.

    Parameters:
    base (float): The base of the triangle.
    height (float): The height of the triangle.

    Returns:
    float: The calculated area of the triangle.
    """
    return 0.5 * base * height

class TestTriangleArea(unittest.TestCase):
    def test_normal_case_positive_base_height(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

    def test_normal_case_zero_base(self):
        self.assertEqual(triangle_area(0, 10), 0.0)

    def test_normal_case_zero_height(self):
        self.assertEqual(triangle_area(10, 0), 0.0)

    def test_normal_case_negative_base_height(self):
        self.assertEqual(triangle_area(-5, -3), 7.5)

    def test_error_handling_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            triangle_area('a', 'b')

if __name__ == '__main__':
    unittest.main()