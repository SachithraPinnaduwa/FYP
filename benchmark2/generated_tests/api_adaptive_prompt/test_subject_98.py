from subject_98 import *

import unittest

class TestTriangleFunctions(unittest.TestCase):
    def test_is_right_triangle(self):
        self.assertTrue(is_right_triangle(3, 4, 5))
        self.assertFalse(is_right_triangle(3, 4, 6))
        self.assertFalse(is_right_triangle(0, 0, 0))
        self.assertFalse(is_right_triangle(-3, -4, -5))
        self.assertTrue(is_right_triangle(3.5, 4.5, 5.5))
        with self.assertRaises(TypeError):
            is_right_triangle('a', 'b', 'c')
        with self.assertRaises(TypeError):
            is_right_triangle(3, 4)
        with self.assertRaises(TypeError):
            is_right_triangle(3, 4, 5, 6)

    def test_is_equilateral_triangle(self):
        self.assertTrue(is_equilateral_triangle(5, 5, 5))
        self.assertFalse(is_equilateral_triangle(3, 4, 5))
        self.assertFalse(is_equilateral_triangle(0, 0, 0))
        self.assertFalse(is_equilateral_triangle(-3, -4, -5))
        self.assertTrue(is_equilateral_triangle(3.5, 3.5, 3.5))
        with self.assertRaises(TypeError):
            is_equilateral_triangle('a', 'b', 'c')
        with self.assertRaises(TypeError):
            is_equilateral_triangle(3, 4)
        with self.assertRaises(TypeError):
            is_equilateral_triangle(3, 4, 5, 6)

    def test_is_isosceles_triangle(self):
        self.assertTrue(is_isosceles_triangle(5, 5, 3))
        self.assertFalse(is_isosceles_triangle(3, 4, 5))
        self.assertFalse(is_isosceles_triangle(0, 0, 0))
        self.assertFalse(is_isosceles_triangle(-3, -4, -5))
        self.assertTrue(is_isosceles_triangle(3.5, 3.5, 3.5))
        with self.assertRaises(TypeError):
            is_isosceles_triangle('a', 'b', 'c')
        with self.assertRaises(TypeError):
            is_isosceles_triangle(3, 4)
        with self.assertRaises(TypeError):
            is_isosceles_triangle(3, 4, 5, 6)

    def test_calculate_area(self):
        self.assertAlmostEqual(calculate_area(5), 10.825317547305485)
        self.assertAlmostEqual(calculate_area(3.5), 10.825317547305485)
        with self.assertRaises(TypeError):
            calculate_area('a')

    def test_calculate_perimeter(self):
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)
        self.assertEqual(calculate_perimeter(3.5, 4.5, 5.5), 13.5)
        with self.assertRaises(TypeError):
            calculate_perimeter('a', 'b', 'c')
        with self.assertRaises(TypeError):
            calculate_perimeter(3, 4)
        with self.assertRaises(TypeError):
            calculate_perimeter(3, 4, 5, 6)

    def test_calculate_angles(self):
        angles = calculate_angles(3, 4, 5)
        self.assertAlmostEqual(angles[0], 36.86989764584402)
        self.assertAlmostEqual(angles[1], 53.13010235415598)
        self.assertAlmostEqual(angles[2], 90.0)
        angles = calculate_angles(5, 5, 3)
        self.assertAlmostEqual(angles[0], 75.52248781407007)
        self.assertAlmostEqual(angles[1], 75.52248781407007)
        self.assertAlmostEqual(angles[2], 28.95502437185986)
        with self.assertRaises(TypeError):
            calculate_angles('a', 'b', 'c')
        with self.assertRaises(TypeError):
            calculate_angles(3, 4)
        with self.assertRaises(TypeError):
            calculate_angles(3, 4, 5, 6)

if __name__ == '__main__':
    unittest.main()