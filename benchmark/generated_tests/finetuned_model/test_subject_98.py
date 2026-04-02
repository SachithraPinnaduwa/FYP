import math
import unittest

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
    area = (math.sqrt(3) / 4) * a**2
    return area

def calculate_perimeter(a, b, c):
    perimeter = a + b + c
    return perimeter

def calculate_angles(a, b, c):
    angle_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_c = 180 - angle_a - angle_b
    return angle_a, angle_b, angle_c

class TestTriangleFunctions(unittest.TestCase):
    def test_is_right_triangle(self):
        self.assertTrue(is_right_triangle(3, 4, 5))
        self.assertTrue(is_right_triangle(5, 12, 13))
        self.assertTrue(is_right_triangle(8, 15, 17))
        self.assertFalse(is_right_triangle(6, 7, 8))
        self.assertFalse(is_right_triangle(9, 12, 15))

    def test_is_equilateral_triangle(self):
        self.assertTrue(is_equilateral_triangle(3, 3, 3))
        self.assertFalse(is_equilateral_triangle(3, 4, 5))
        self.assertFalse(is_equilateral_triangle(5, 5, 7))

    def test_is_isosceles_triangle(self):
        self.assertTrue(is_isosceles_triangle(3, 3, 5))
        self.assertTrue(is_isosceles_triangle(5, 3, 5))
        self.assertTrue(is_isosceles_triangle(3, 5, 5))
        self.assertFalse(is_isosceles_triangle(3, 4, 5))
        self.assertFalse(is_isosceles_triangle(5, 6, 7))

    def test_calculate_area(self):
        self.assertAlmostEqual(calculate_area(3), 3.897114317029974)
        self.assertAlmostEqual(calculate_area(4), 6.928203230275509)
        self.assertAlmostEqual(calculate_area(5), 10.825317547305485)

    def test_calculate_perimeter(self):
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)
        self.assertEqual(calculate_perimeter(5, 12, 13), 30)
        self.assertEqual(calculate_perimeter(8, 15, 17), 40)

    def test_calculate_angles(self):
        self.assertAlmostEqual(calculate_angles(3, 4, 5), (36.86989764584409, 53.13010235415591, 90.0))
        self.assertAlmostEqual(calculate_angles(5, 12, 13), (22.61986494804042, 67.38013505195958, 90.0))
        self.assertAlmostEqual(calculate_angles(8, 15, 17), (28.955026298901035, 50.527541301098965, 100.51743240000001))

if __name__ == '__main__':
    unittest.main()