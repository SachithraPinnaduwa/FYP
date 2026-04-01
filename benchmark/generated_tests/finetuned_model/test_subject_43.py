import unittest

class TestTriangleAreaFunction(unittest.TestCase):
    # Test case with positive base and height
    def test_triangle_area_positive(self):
        # Arrange
        base = 10
        height = 5
        expected_area = 25.0

        # Act
        actual_area = triangle_area(base, height)

        # Assert
        self.assertEqual(actual_area, expected_area)

    # Test case with zero base
    def test_triangle_area_zero_base(self):
        # Arrange
        base = 0
        height = 5
        expected_area = 0.0

        # Act
        actual_area = triangle_area(base, height)

        # Assert
        self.assertEqual(actual_area, expected_area)

    # Test case with zero height
    def test_triangle_area_zero_height(self):
        # Arrange
        base = 10
        height = 0
        expected_area = 0.0

        # Act
        actual_area = triangle_area(base, height)

        # Assert
        self.assertEqual(actual_area, expected_area)

    # Test case with negative base
    def test_triangle_area_negative_base(self):
        # Arrange
        base = -10
        height = 5
        expected_area = 25.0

        # Act
        actual_area = triangle_area(base, height)

        # Assert
        self.assertEqual(actual_area, expected_area)

    # Test case with negative height
    def test_triangle_area_negative_height(self):
        # Arrange
        base = 10
        height = -5
        expected_area = 25.0

        # Act
        actual_area = triangle_area(base, height)

        # Assert
        self.assertEqual(actual_area, expected_area)

    # Test case with floating point numbers
    def test_triangle_area_floating_point(self):
        # Arrange
        base = 10.5
        height = 5.2
        expected_area = 27.3

        # Act
        actual_area = triangle_area(base, height)

        # Assert
        self.assertAlmostEqual(actual_area, expected_area, places=1)