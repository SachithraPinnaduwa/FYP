from subject_98 import *

import unittest
from math import sqrt, degrees, acos

def is_right_triangle(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    elif b**2 + c**2 == a**2:
        return True
    elif a**2 + c**2 == b**2:
        return True
    else:
        return False

def is_equilateral_triangle(a, b, c):
    if a == b and b == c:
        return True
    else:
        return False

def is_isosceles_triangle(a, b, c):
    if a == b or b == c or a == c:
        return True
    else:
        return False

def calculate_area(a):
    area = (sqrt(3) / 4) * a**2
    return area

def calculate_perimeter(a, b, c):
    perimeter = a + b + c
    return perimeter

def calculate_angles(a, b, c):
    angle_a = degrees(acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_b = degrees(acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_c = 180 - angle_a - angle_b
    return angle_a, angle_b, angle_c

class TestTriangleFunctions(unittest.TestCase):
    def test_is_right_triangle(self):
        self.assertTrue(is_right_triangle(3, 4, 5))
        self.assertTrue(is_right_triangle(5, 12, 13))
        self.assertFalse(is_right_triangle(1, 2, 3))

    def test_is_equilateral_triangle(self):
        self.assertTrue(is_equilateral_triangle(3, 3, 3))
        self.assertFalse(is_equilateral_triangle(3, 4, 5))

    def test_is_isosceles_triangle(self):
        self.assertTrue(is_isosceles_triangle(3, 3, 5))
        self.assertTrue(is_isosceles_triangle(3, 5, 3))
        self.assertTrue(is_isosceles_triangle(5, 3, 3))
        self.assertFalse(is_isosceles_triangle(3, 4, 5))

    def test_calculate_area(self):
        self.assertAlmostEqual(calculate_area(3), 3.897114317029974)
        self.assertAlmostEqual(calculate_area(5), 10.825317547305485)

    def test_calculate_perimeter(self):
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)
        self.assertEqual(calculate_perimeter(5, 12, 13), 30)

    def test_calculate_angles(self):
        self.assertAlmostEqual(calculate_angles(3, 4, 5), (37.00000000000001, 53.00000000000001, 90.0))
        self.assertAlmostEqual(calculate_angles(5, 12, 13), (22.61986494804043, 67.38013505195957, 90.0))

if __name__ == '__main__':
    unittest.main()