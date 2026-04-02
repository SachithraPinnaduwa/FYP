```python
import unittest

class TestCountAndIndices(unittest.TestCase):
    def test_count_and_indices(self):
        arr = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
        target = 4
        count, indices = count_and_indices(arr, target)
        self.assertEqual(count, 4)
        self.assertEqual(indices, [3, 7, 8, 9])

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 10
        count, indices = count_and_indices(arr, target)
        self.assertEqual(count, 1)
        self.assertEqual(indices, [9])

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 1
        count, indices = count_and_indices(arr, target)
        self.assertEqual(count, 0)
        self.assertEqual(indices, [])

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 100
        count, indices = count_and_indices(arr, target)
        self.assertEqual(count, 0)
        self.assertEqual(indices, [])

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 0
        count, indices = count_and_indices(arr, target)
        self.assertEqual(count, 0)
        self.assertEqual(indices, [])

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 11
        count, indices = count_and_indices(arr, target)
        self.assertEqual(count, 0)
        self.assertEqual(indices, [])

        arr = [1, 2, 3, 4,