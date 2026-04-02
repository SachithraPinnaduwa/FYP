import unittest

class TestPolynomial(unittest.TestCase):
    """
    Test suite for the polynomial function.
    """

    def test_degree_4(self):
        """
        Test the polynomial function with a degree 4 equation.
        """
        x = 2
        a, b, c, d, e = 1, 2, 3, 4, 5
        result = polynomial(x, a, b, c, d, e)
        expected = 1 * 2**4 + 2 * 2**3 + 3 * 2**2 + 4 * 2 + 5
        self.assertEqual(result, expected)

    def test_degree_3(self):
        """
        Test the polynomial function with a degree 3 equation.
        """
        x = 3
        a, b, c, d, e = 0, 1, 2, 3, 4
        result = polynomial(x, a, b, c, d, e)
        expected = 1 * 3**3 + 2 * 3**2 + 3 * 3 + 4
        self.assertEqual(result, expected)

    def test_degree_2(self):
        """
        Test the polynomial function with a degree 2 equation.
        """
        x = 4
        a, b, c, d, e = 0, 0, 1, 2, 3
        result = polynomial(x, a, b, c, d, e)
        expected = 1 * 4**2 + 2 * 4 + 3
        self.assertEqual(result, expected)

    def test_degree_1(self):
        """
        Test the polynomial function with a degree 1 equation.
        """
        x = 5
        a, b, c, d, e = 0, 0, 0, 1, 2
        result = polynomial(x, a, b, c, d, e)
        expected = 1 * 5 + 2
        self.assertEqual(result, expected)

    def test_degree_0(self):
        """
        Test the polynomial function with a degree 0 equation.
        """
        x = 6
        a, b, c, d, e = 0, 0, 0, 0, 1
        result = polynomial(x, a, b, c, d, e)
        expected = 1
        self.assertEqual(result, expected)

    def test_negative_coefficients(self):
        """
        Test the polynomial function with negative coefficients.
        """
        x = 2
        a, b, c, d, e = -1, -2, -3, -4, -5
        result = polynomial(x, a, b, c, d, e)
        expected = -1 * 2**4 - 2 * 2**3 - 3 * 2**2 - 4 * 2 - 5
        self.assertEqual(result, expected)

    def test_zero_coefficients(self):
        """
        Test the polynomial function with zero coefficients.
        """
        x = 3
        a, b, c, d, e = 0, 0, 0, 0, 0
        result = polynomial(x, a, b, c, d, e)
        expected = 0
        self.assertEqual(result, expected)

    def test_large_values(self):
        """
        Test the polynomial function with large values.
        """
        x = 10
        a, b, c, d, e = 1, 2, 3, 4, 5
        result = polynomial(x, a, b, c, d, e)
        expected = 1 * 10**4 + 2 * 10**3 + 3 * 10**2 + 4 * 10 + 5
        self.assertEqual(result, expected)

    def test_small_values(self):
        """
        Test the polynomial function with small values.
        """
        x = 0.1
        a, b, c, d, e = 1, 2, 3, 4, 5
        result = polynomial(x, a, b, c, d, e)
        expected = 1 * 0.1**4 + 2 * 0.1**3 + 3 * 0.1**2 + 4 * 0.1 + 5
        self.assertEqual(result, expected)

    def test_negative_x(self):
        """
        Test the polynomial function with negative x values.
        """
        x = -2
        a, b, c, d, e = 1, 2, 3, 4, 5
        result = polynomial(x, a, b, c, d, e)
        expected = 1 * (-2)**4 + 2 * (-2)**3 + 3 * (-2)**2 + 4 * (-2) + 5
        self.assertEqual(result, expected)

    def test_float_coefficients(self):
        """
        Test the polynomial function with float coefficients.
        """
        x = 2
        a, b, c, d, e = 1.5, 2.5, 3.5, 4.5, 5.5
        result = polynomial(x, a, b, c, d, e)
        expected = 1.5 * 2**4 + 2.5 * 2**3 + 3.5 * 2**2 + 4.5 * 2 + 5.5
        self.assertEqual(result, expected)

    def test_mixed_coefficients(self):
        """
        Test the polynomial function with mixed coefficients.
        """
        x = 3
        a, b, c, d, e = 1, -2, 3, -4, 5
        result = polynomial(x, a, b, c, d, e)
        expected = 1 * 3**4 - 2 * 3**3 + 3 * 3**2 - 4 * 3 + 5
        self.assertEqual(result, expected)

    def test_zero_x(self):
        """
        Test the polynomial function with x = 0.
        """
        x = 0
        a, b, c, d, e = 1, 2, 3, 4, 5
        result = polynomial(x, a, b, c, d, e)
        expected = 5
        self.assertEqual(result, expected)

    def test_large_coefficients(self):
        """
        Test the polynomial function with large coefficients.
        """
        x = 2
        a, b, c, d, e = 100, 200, 300, 400, 500