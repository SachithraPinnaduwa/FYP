```python
import unittest

class TestFindMedian(unittest.TestCase):
    def test_find_median(self):
        self.assertEqual(find_median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7]), 4)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8]), 4)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 6)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 6)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 7)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), 7)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 8)
        self.assertEqual(find_median([1, 2