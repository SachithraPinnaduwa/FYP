import unittest

class TestCubicProduct(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(cubic_product(2, 3, 4), 864)

    def test_negative_integers(self):
        self.assertEqual(cubic_product(-1, -2, -3), -216)

    def test_mixed_integers(self):
        self.assertEqual(cubic_product(1, -2, 3), -216)

    def test_zero_values(self):
        self.assertEqual(cubic_product(0, 0, 0), 0)

    def test_floats(self):
        self.assertAlmostEqual(cubic_product(1.5, 2.5, 3.5), 984.375)

    def test_large_numbers(self):
        self.assertEqual(cubic_product(10, 10, 10), 1e+15)

    def test_single_value(self):
        self.assertEqual(cubic_product(5, 1, 1), 125)
        
if __name__ == '__main__':
    unittest.main()