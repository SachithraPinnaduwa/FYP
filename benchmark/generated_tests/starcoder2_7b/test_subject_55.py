```python
import unittest

class TestSmallestPositiveNoCompare(unittest.TestCase):
    def test_smallest_positive_no_compare(self):
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, -5]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, -4, -5]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, -3, -4, -5]), 1)
        self.assertEqual(smallest_positive_no_compare([1, -2, -3, -4, -5]), 1)
        self.assertEqual(smallest_positive_no_compare([-1, -2, -3, -4, -5]), None)
        self.assertEqual(smallest_positive_no_compare([0, 0, 0, 0, 0]), None)
        self.assertEqual(smallest_positive_no_compare([0, 0, 0, 0, 1]), 1)
        self.assertEqual(smallest_positive_no_compare([0, 0, 0, 1, 1]), 1)
        self.assertEqual(smallest_positive_no_compare([0, 0, 1, 1, 1]), 1)
        self.assertEqual(smallest_positive_no_compare([0, 1, 1, 1, 1]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 1, 1, 1, 1]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 1, 1, 1, 2]), 2)
        self.assertEqual(smallest_positive_no_compare([1, 1, 1, 2, 2]), 2)
        self.assertEqual(smallest_positive_no_compare([1, 1, 2, 2, 2]), 2)
        self.assertEqual(smallest_positive_no_compare([