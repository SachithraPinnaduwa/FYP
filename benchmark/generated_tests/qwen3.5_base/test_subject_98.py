import unittest

class TestTriangleFunctions(unittest.TestCase):
    def test_is_right_triangle(self):
        self.assertTrue(is_right_triangle(3, 4, 5))
        self.assertTrue(is_right_triangle(5, 12, 13))
        self.assertFalse(is_right_triangle(3, 4, 6))
        self.assertFalse(is_right_triangle(5, 5, 5))

    def test_is_equilateral_triangle(self):
        self.assertTrue(is_equilateral_triangle(5, 5, 5))
        self.assertFalse(is_equilateral_triangle(3, 4, 5))
        self.assertFalse(is_equilateral_triangle(5, 5, 6))

    def test_is_isosceles_triangle(self):
        self.assertTrue(is_isosceles_triangle(5, 5, 5))
        self.assertTrue(is_isosceles_triangle(3, 4, 4))
        self.assertFalse(is_isosceles_triangle(3, 4, 5))

    def test_calculate_area(self):
        self.assertAlmostEqual(calculate_area(5), 10.825, places=2)
        self.assertAlmostEqual(calculate_area(10), 43.301, places=2)

    def test_calculate_perimeter(self):
        self.assertEqual(calculate_perimeter(5, 5, 5), 15)
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)

    def test_calculate_angles(self):
        angles = calculate_angles(3, 4, 5)
        self.assertAlmostEqual(angles[0], 36.87, places=2)
        self.assertAlmostEqual(angles[1], 53.13, places=2)
        self.assertAlmostEqual(angles[2], 90.0, places=2)

if __name__ == '__main__':
    unittest.main()
