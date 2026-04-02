```python
import unittest

class TestMedian(unittest.TestCase):
    def test_median(self):
        self.assertEqual(median([1, 2, 3], lambda x, y: x - y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x + y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x * y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x / y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x // y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x % y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x ** y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x == y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x!= y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x > y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x < y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x >= y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x <= y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x is y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x is not y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x in y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x not in y), 2)
        self.assertEqual(median([1, 2, 3], lambda x, y: x and y), 2)