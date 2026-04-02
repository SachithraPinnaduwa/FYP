import unittest

class TestTriangleArea(unittest.TestCase):
    def test_triangle_area_with_positive_base_and_height(self):
        # Test case with positive base and height
        self.assertEqual(triangle_area(5, 3), 7.5)

    def test_triangle_area_with_negative_base_and_positive_height(self):
        # Test case with negative base and positive height
        self.assertEqual(triangle_area(-5, 3), -7.5)

    def test_triangle_area_with_positive_base_and_negative_height(self):
        # Test case with positive base and negative height
        self.assertEqual(triangle_area(5, -3), -7.5)

    def test_triangle_area_with_negative_base_and_negative_height(self):
        # Test case with negative base and negative height
        self.assertEqual(triangle_area(-5, -3), 7.5)

    def test_triangle_area_with_zero_base_and_non_zero_height(self):
        # Test case with zero base and non-zero height
        self.assertEqual(triangle_area(0, 3), 0)

    def test_triangle_area_with_non_zero_base_and_zero_height(self):
        # Test case with non-zero base and zero height
        self.assertEqual(triangle_area(5, 0), 0)

    def test_triangle_area_with_zero_base_and_zero_height(self):
        # Test case with zero base and zero height
        self.assertEqual(triangle_area(0, 0), 0)

if __name__ == '__main__':
    unittest.main()