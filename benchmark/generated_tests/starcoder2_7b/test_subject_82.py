import unittest

class TestPolynomial(unittest.TestCase):
    def test_polynomial(self):
        self.assertEqual(polynomial(1, 1, 1, 1, 1, 1), 6)
        self.assertEqual(polynomial(2, 1, 1, 1, 1, 1), 22)
        self.assertEqual(polynomial(3, 1, 1, 1, 1, 1), 50)
        self.assertEqual(polynomial(4, 1, 1, 1, 1, 1), 98)
        self.assertEqual(polynomial(5, 1, 1, 1, 1, 1), 170)

if __name__ == '__main__':
    unittest.main()