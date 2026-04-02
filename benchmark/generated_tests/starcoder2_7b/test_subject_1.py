```python
import unittest

class TestMedianInInterval(unittest.TestCase):
    def test_median_in_interval(self):
        self.assertEqual(median_in_interval([1, 2, 3, 4, 5], 2, 4), True)
        self.assertEqual(median_in_interval([1, 2, 3, 4, 5], 3, 4), False)
        self.assertEqual(median_in_interval([1, 2, 3, 4, 5], 1, 5), True)
        self.assertEqual(median_in_interval([1, 2, 3, 4, 5], 1, 6), False)
        self.assertEqual(median_in_interval([1, 2, 3, 4, 5], 0, 6), True)
        self.assertEqual(median_in_interval([1, 2, 3, 4, 5], 0, 7), False)
        self.assertEqual(median_in_interval([1, 2, 3, 4, 5], 0, 5), True)
        self.assertEqual(median_in_interval([1, 2, 3, 4, 5], 0, 4), False)
        self.assertEqual(median_in_interval([1, 2, 3, 4, 5], 0, 3), True)
        self.assertEqual(median_in_interval([1, 2, 3, 4, 5], 0, 2), False)
        self.assertEqual(median_in_interval([1, 2, 3, 4, 5], 0, 1), True)
        self.assertEqual(median_in_interval([1, 2, 3, 4, 5], 0, 0), False)
        self.assertEqual(median_in_interval([1, 2, 3, 4, 5], 2, 2), True)
        self.assertEqual(median_in_interval([1, 2, 3, 4, 5], 2, 3), False)
        self.assertEqual(median_in_interval([1, 2, 3,