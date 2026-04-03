```python
import unittest

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 5
        self.assertEqual(binary_search(arr, target), 4)

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 11
        self.assertEqual(binary_search(arr, target), -1)

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 1
        self.assertEqual(binary_search(arr, target), 0)

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 10
        self.assertEqual(binary_search(arr, target), 9)

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 10
        self.assertEqual(binary_search(arr, target), 9)

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 10
        self.assertEqual(binary_search(arr, target), 9)

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 10
        self.assertEqual(binary_search(arr, target), 9)

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 10
        self.assertEqual(binary_search(arr, target), 9)

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 1