import unittest

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area_with_positive_values(self):
        self.assertEqual(triangle_area(10, 5), 25.0)
        self.assertEqual(triangle_area(7, 3), 10.5)

    def test_triangle_area_with_zero_base(self):
        self.assertEqual(triangle_area(0, 5), 0.0)
        self.assertEqual(triangle_area(0, 0), 0.0)

    def test_triangle_area_with_negative_height(self):
        with self.assertRaises(ValueError):
            triangle_area(10, -5)

    def test_triangle_area_with_non_numeric_input(self):
        with self.assertRaises(TypeError):
            triangle_area('a', 5)
        with self.assertRaises(TypeError):
            triangle_area(10, 'b')
        with self.assertRaises(TypeError):
            triangle_area(None, 5)
        with self.assertRaises(TypeError):
            triangle_area(10, None)

if __name__ == '__main__':
    unittest.main()