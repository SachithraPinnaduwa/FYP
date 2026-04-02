import unittest

class TestPolynomial(unittest.TestCase):
    def test_polynomial_with_positive_coefficients(self):
        self.assertAlmostEqual(polynomial(2, 1, 2, 3, 4, 5), 65)
        self.assertAlmostEqual(polynomial(3, 1, 1, 1, 1, 1), 121)

    def test_polynomial_with_negative_coefficients(self):
        self.assertAlmostEqual(polynomial(-1, -1, -1, -1, -1, -1), -1)
        self.assertAlmostEqual(polynomial(-2, -1, 2, -3, 4, -5), 15)

    def test_polynomial_with_mixed_coefficients(self):
        self.assertAlmostEqual(polynomial(0, 1, -2, 3, -4, 5), 5)
        self.assertAlmostEqual(polynomial(1, 0, 1, 0, 1, 0), 2)

    def test_polynomial_with_zero_coefficients(self):
        self.assertAlmostEqual(polynomial(0, 0, 0, 0, 0, 5), 5)
        self.assertAlmostEqual(polynomial(1, 0, 0, 0, 0, 0), 0)

    def test_polynomial_with_large_coefficients(self):
        self.assertAlmostEqual(polynomial(10, 1000, 2000, 3000, 4000, 5000), 15000000)
        self.assertAlmostEqual(polynomial(100, 1, 0, 0, 0, 0), 100000001)

if __name__ == '__main__':
    unittest.main()