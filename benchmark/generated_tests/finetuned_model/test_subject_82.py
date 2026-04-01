import unittest

class TestPolynomialFunction(unittest.TestCase):
    # Test case with integer coefficients and x value
    def test_polynomial_integers(self):
        # Arrange
        x = 2
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        expected_result = 1*2**4 + 2*2**3 + 3*2**2 + 4*2 + 5
        
        # Act
        result = polynomial(x, a, b, c, d, e)
        
        # Assert
        self.assertEqual(result, expected_result)

    # Test case with floating-point coefficients and x value
    def test_polynomial_floats(self):
        # Arrange
        x = 3.5
        a = 0.5
        b = 1.2
        c = 2.3
        d = 3.4
        e = 4.5
        expected_result = 0.5*3.5**4 + 1.2*3.5**3 + 2.3*3.5**2 + 3.4*3.5 + 4.5
        
        # Act
        result = polynomial(x, a, b, c, d, e)
        
        # Assert
        self.assertAlmostEqual(result, expected_result)

    # Test case with coefficients equal to zero
    def test_polynomial_zero_coefficients(self):
        # Arrange
        x = 0
        a = 0
        b = 0
        c = 0
        d = 0
        e = 5
        expected_result = 5
        
        # Act
        result = polynomial(x, a, b, c, d, e)
        
        # Assert
        self.assertEqual(result, expected_result)

    # Test case with x equal to zero
    def test_polynomial_zero_x(self):
        # Arrange
        x = 0
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        expected_result = 5
        
        # Act
        result = polynomial(x, a, b, c, d, e)
        
        # Assert
        self.assertEqual(result, expected_result)

    # Test case with coefficients and x values equal to one
    def test_polynomial_one(self):
        # Arrange
        x = 1
        a = 1
        b = 1
        c = 1
        d = 1
        e = 1
        expected_result = 1*1**4 + 1*1**3 + 1*1**2 + 1*1 + 1
        
        # Act
        result = polynomial(x, a, b, c, d, e)
        
        # Assert
        self.assertEqual(result, expected_result)