import unittest
from triangle import is_right_triangle, is_equilateral_triangle, is_isosceles_triangle, calculate_area, calculate_perimeter, calculate_angles

class TestTriangleFunctions(unittest.TestCase):

    def test_is_right_triangle(self):
        self.assertTrue(is_right_triangle(3, 4, 5))
        self.assertFalse(is_right_triangle(1, 2, 3))

    def test_is_equilateral_triangle(self):
        self.assertTrue(is_equilateral_triangle(5, 5, 5))
        self.assertFalse(is_equilateral_triangle(1, 2, 3))

    def test_is_isosceles_triangle(self):
        self.assertTrue(is_isosceles_triangle(5, 5, 3))
        self.assertFalse(is_isosceles_triangle(1, 2, 3))

    def test_calculate_area(self):
        self.assertAlmostEqual(calculate_area(5), 10.8253)
        self.assertNotEqual(calculate_area(5), 10)

    def test_calculate_perimeter(self):
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)
        self.assertNotEqual(calculate_perimeter(3, 4, 5), 10)

    def test_calculate_angles(self):
        self.assertTupleAlmostEquals(calculate_angles(3, 4, 5), (36.87, 53.13, 90.00), places=2)
        self.assertNotEqual(calculate_angles(3, 4, 5), (30, 60, 90))

if __name__ == '__main__':
    unittest.main()