import unittest

def cubic_product(a, b, c):
    return (a**3) * (b**3) * (c**3)

class TestCubicProduct(unittest.TestCase):
    def test_with_integers(self):
        self.assertEqual(cubic_product(2, 3, 4), 8 * 27 * 64)
        self.assertEqual(cubic_product(1, 1, 1), 1)
        self.assertEqual(cubic_product(0, 0, 0), 0)

    def test_with_floats(self):
        self.assertAlmostEqual(cubic_product(1.5, 2.5, 3.5), 3375.0, places=6)
        self.assertAlmostEqual(cubic_product(-1.1, 2.2, -3.3), -10648.03125, places=6)

    def test_with_negative_numbers(self):
        self.assertEqual(cubic_product(-1, -2, -3), -8)
        self.assertEqual(cubic_product(-2, 3, 4), -1728)

    def test_with_large_numbers(self):
        self.assertEqual(cubic_product(10, 100, 1000), 1e21)
        self.assertEqual(cubic_product(10000, 100000, 1000000), 1e24)

    def test_with_one_variable(self):
        self.assertEqual(cubic_product(5, 1, 1), 125)
        self.assertEqual(cubic_product(1, 3, 1), 27)

if __name__ == '__main__':
    unittest.main()