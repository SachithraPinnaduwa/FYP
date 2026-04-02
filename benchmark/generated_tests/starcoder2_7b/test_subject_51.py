```python
import unittest

class TestSumListRecursive(unittest.TestCase):
    def test_sum_list_recursive(self):
        self.assertEqual(sum_list_recursive([1, 2, 3]), 6)
        self.assertEqual(sum_list_recursive([1, 2, 3, 4]), 10)
        self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5, 6]), 21)
        self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5, 6, 7]), 28)
        self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5, 6, 7, 8]), 36)
        self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9]), 45)
        self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)
        self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 66)
        self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 78)
        self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 91)
        self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1