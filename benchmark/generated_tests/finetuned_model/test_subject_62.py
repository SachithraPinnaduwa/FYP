import unittest

class TestCubicProductFunction(unittest.TestCase):
    # Test case with integer inputs
    def test_cubic_product_integers(self):
        # Arrange
        a = 2
        b = 3
        c = 4
        expected_result = 2 * 3 * 4 * 2 * 3 * 4 * 2 * 3 * 4
        
        # Act
        result = cubic_product(a, b, c)
        
        # Assert
        self.assertEqual(result, expected_result)

    # Test case with floating-point inputs
    def test_cubic_product_floats(self):
        # Arrange
        a = 2.5
        b = 3.5
        c = 4.5
        expected_result = a**3 * b**3 * c**3
        
        # Act
        result = cubic_product(a, b, c)
        
        # Assert
        self.assertAlmostEqual(result, expected_result)

    # Test case with negative inputs
    def test_cubic_product_negative(self):
        # Arrange
        a = -2
        b = -3
        c = -4
        expected_result = (-2)**3 * (-3)**3 * (-4)**3
        
        # Act
        result = cubic_product(a, b, c)
        
        # Assert
        self.assertEqual(result, expected_result)

    # Test case with zero inputs
    def test_cubic_product_zero(self):
        # Arrange
        a = 0
        b = 0
        c = 0
        expected_result = 0
        
        # Act
        result = cubic_product(a, b, c)
        
        # Assert
        self.assertEqual(result, expected_result)

    # Test case with large inputs
    def test_cubic_product_large(self):
        # Arrange
        a = 1000
        b = 2000
        c = 3000
        expected_result = a**3 * b**3 * c**3
        
        # Act
        result = cubic_product(a, b, c)
        
        # Assert
        self.assertEqual(result, expected_result)