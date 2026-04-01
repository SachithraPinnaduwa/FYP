import unittest

class TestPolynomial(unittest.TestCase):
    def test_polynomial(self):
        # Test case 1: Simple positive values
        self.assertEqual(polynomial(1, 1, 0, 0, 0, 0), 1)
        
        # Test case 2: Coefficient of x^4 is not zero
        self.assertEqual(polynomial(2, 1, 0, 0, 0, 0), 16)
        
        # Test case 3: All coefficients are non-zero
        self.assertEqual(polynomial(2, 1, 2, 3, 4, 5), 1*2**4 + 2*2**3 + 3*2**2 + 4*2 + 5)
        
        # Test case 4: Negative value of x
        self.assertEqual(polynomial(-1, 1, 0, 0, 0, 0), -1)
        
        # Test case 5: Zero value of x
        self.assertEqual(polynomial(0, 1, 2, 3, 4, 5), 5)
        
        # Test case 6: Large value of x
        self.assertEqual(polynomial(10, 1, 0, 0, 0, 0), 10000)
        
        # Test case 7: Decimal values
        self.assertAlmostEqual(polynomial(0.5, 1, 1, 1, 1, 1), 1.9375)
        
        # Test case 8: Edge case where all coefficients except e are zero
        self.assertEqual(polynomial(1, 0, 0, 0, 0, 1), 1)

if __name__ == '__main__':
    unittest.main()