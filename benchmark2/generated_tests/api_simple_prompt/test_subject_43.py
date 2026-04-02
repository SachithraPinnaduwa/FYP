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
    def test_triangle_area(self):
        self.assertEqual(triangle_area(10, 5), 25.0)
        self.assertEqual(triangle_area(7, 3), 10.5)
        self.assertEqual(triangle_area(0, 5), 0.0)
        self.assertEqual(triangle_area(10, 0), 0.0)
        self.assertEqual(triangle_area(4.5, 3.2), 7.2)

if __name__ == '__main__':
    unittest.main()