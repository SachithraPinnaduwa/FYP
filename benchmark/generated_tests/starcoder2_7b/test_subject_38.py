```python
import unittest

class TestCalculateArea(unittest.TestCase):
    def test_calculate_area(self):
        self.assertEqual(calculate_area(3), 2.30)
        self.assertEqual(calculate_area(10), 25.00)
        self.assertEqual(calculate_area(100), 1250.00)
        self.assertEqual(calculate_area(1000), 31250.00)
        self.assertEqual(calculate_area(10000), 312500.00)
        self.assertEqual(calculate_area(100000), 3125000.00)
        self.assertEqual(calculate_area(1000000), 31250000.00)
        self.assertEqual(calculate_area(10000000), 312500000.00)
        self.assertEqual(calculate_area(100000000), 3125000000.00)
        self.assertEqual(calculate_area(1000000000), 31250000000.00)
        self.assertEqual(calculate_area(10000000000), 312500000000.00)
        self.assertEqual(calculate_area(100000000000), 3125000000000.00)
        self.assertEqual(calculate_area(1000000000000), 31250000000000.00)
        self.assertEqual(calculate_area(10000000000000), 312500000000000.00)
        self.assertEqual(calculate_area(100000000000000), 3125000000000000.00)
        self.assertEqual(calculate_