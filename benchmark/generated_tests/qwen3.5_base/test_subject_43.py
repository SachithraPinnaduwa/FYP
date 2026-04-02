import unittest

class TestTriangleArea(unittest.TestCase):
    """
    Test suite for the triangle_area function.
    """

    def test_positive_values(self):
        """Test with positive base and height values."""
        self.assertEqual(triangle_area(10, 5), 25)
        self.assertEqual(triangle_area(100, 100), 5000)

    def test_zero_values(self):
        """Test with zero base or height values."""
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(10, 0), 0)

    def test_negative_values(self):
        """Test with negative base or height values."""
        self.assertEqual(triangle_area(-10, 5), -25)
        self.assertEqual(triangle_area(10, -5), -25)

    def test_large_values(self):
        """Test with large base and height values."""
        self.assertEqual(triangle_area(1000, 1000), 500000)

    def test_float_values(self):
        """Test with float base and height values."""
        self.assertEqual(triangle_area(10.5, 5.2), 27.3)

    def test_invalid_input_types(self):
        """Test with invalid input types."""
        with self.assertRaises(TypeError):
            triangle_area("10", 5)
        with self.assertRaises(TypeError):
            triangle_area(10, "5")

if __name__ == '__main__':
    unittest.main()
