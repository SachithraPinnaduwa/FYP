```python
import unittest

class TestCubicProduct(unittest.TestCase):
    def test_cubic_product(self):
        self.assertEqual(cubic_product(2, 3, 4), 512)
        self.assertEqual(cubic_product(1, 2, 3), 27)
        self.assertEqual(cubic_product(1, 1, 1), 1)
        self.assertEqual(cubic_product(0, 0, 0), 0)
        self.assertEqual(cubic_product(-1, -2, -3), -1)
        self.assertEqual(cubic_product(-1, 2, 3), -1)
        self.assertEqual(cubic_product(1, -2, 3), -1)
        self.assertEqual(cubic_product(1, 2, -3), -1)
        self.assertEqual(cubic_product(-1, -2, 3), -1)
        self.assertEqual(cubic_product(-1, 2, -3), -1)
        self.assertEqual(cubic_product(1, -2, -3), -1)
        self.assertEqual(cubic_product(-1, -2, -3), -1)
        self.assertEqual(cubic_product(1, 2, 3), 1)
        self.assertEqual(cubic_product(1, 2, 3), 1)
        self.assertEqual(cubic_product(1, 2, 3), 1)
        self.assertEqual(cubic_product(1, 2, 3), 1)
        self.assertEqual(cubic_product(1, 2, 3), 1)
        self.assertEqual(cubic_product(1, 2, 3), 1)
        self.assertEqual(cubic_product(1, 2, 3), 1)
        self.assertEqual(cubic_product(1, 2, 3), 1)
        self.assertEqual(cubic_product(1, 2, 3), 1)
        self.assertEqual(cubic_product(1, 2, 3), 1)
        self.assertEqual(cubic_product(1, 2, 3), 1)
        self.assertEqual(cubic_product(1, 2, 3), 1)
        self