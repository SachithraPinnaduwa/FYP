from subject_75 import *

import unittest

class TestReverseArray(unittest.TestCase):
    def test_reverseArray(self):
        # Test case 1: Single element array
        arr = [1]
        reverseArray(arr, 0, 0)
        self.assertEqual(arr, [1])

        # Test case 2: Two elements array
        arr = [1, 2]
        reverseArray(arr, 0, 1)
        self.assertEqual(arr, [2, 1])

        # Test case 3: Odd number of elements
        arr = [1, 2, 3, 4, 5]
        reverseArray(arr, 0, 4)
        self.assertEqual(arr, [5, 4, 3, 2, 1])

        # Test case 4: Even number of elements
        arr = [1, 2, 3, 4]
        reverseArray(arr, 0, 3)
        self.assertEqual(arr, [4, 3, 2, 1])

        # Test case 5: Reverse in-place
        arr = [1, 2, 3, 4, 5, 6]
        reverseArray(arr, 1, 4)
        self.assertEqual(arr, [1, 5, 4, 3, 2, 6])

        # Test case 6: Already reversed
        arr = [5, 4, 3, 2, 1]
        reverseArray(arr, 0, 4)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

        # Test case 7: Empty array
        arr = []
        reverseArray(arr, 0, 0)
        self.assertEqual(arr, [])

        # Test case 8: Single element out of bounds
        arr = [1]
        reverseArray(arr, 1, 1)
        self.assertEqual(arr, [1])

        # Test case 9: Negative start index
        arr = [1, 2, 3, 4, 5]
        reverseArray(arr, -1, 4)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

        # Test case 10: End index out of bounds
        arr = [1, 2, 3, 4, 5]
        reverseArray(arr, 0, 5)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()