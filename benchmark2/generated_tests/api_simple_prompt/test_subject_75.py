from subject_75 import *

import unittest

def reverseArray(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseArray(arr, start + 1, end - 1)

class TestReverseArray(unittest.TestCase):
    def test_reverseArray(self):
        arr = [1, 2, 3, 4, 5]
        reverseArray(arr, 0, 4)
        self.assertEqual(arr, [5, 4, 3, 2, 1])

        arr = [10, 20, 30, 40, 50, 60]
        reverseArray(arr, 1, 4)
        self.assertEqual(arr, [10, 50, 40, 30, 20, 60])

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        reverseArray(arr, 2, 6)
        self.assertEqual(arr, [1, 2, 7, 6, 5, 4, 3, 8, 9])

        arr = [100, 200, 300, 400, 500]
        reverseArray(arr, 0, 4)
        self.assertEqual(arr, [500, 400, 300, 200, 100])

        arr = [1]
        reverseArray(arr, 0, 0)
        self.assertEqual(arr, [1])

        arr = []
        reverseArray(arr, 0, -1)
        self.assertEqual(arr, [])

if __name__ == '__main__':
    unittest.main()