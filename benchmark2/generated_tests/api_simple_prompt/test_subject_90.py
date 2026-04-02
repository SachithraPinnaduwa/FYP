from subject_90 import *

import unittest

class TestTransformArrayAfterOperations(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(transform_array_after_operations([-4, 0, -1, 0], 2), [0, 4, 3, 4])
        self.assertEqual(transform_array_after_operations([0, -1, 0, 0, -1, -1, -1, -1, 1, -1], 1), [1, 2, 1, 1, 2, 2, 2, 2, 0, 2])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 1), [4, 3, 2, 1, 0])
        self.assertEqual(transform_array_after_operations([10, 10, 10], 3), [0, 0, 0])
        self.assertEqual(transform_array_after_operations([-1, -2, -3, -4, -5], 1), [6, 5, 4, 3, 2])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 5), [0, 0, 0, 0, 0])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 10), [0, 0, 0, 0, 0])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 100), [0, 0, 0, 0, 0])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 1000), [0, 0, 0, 0, 0])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 10000), [0, 0, 0, 0, 0])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 100000), [0, 0, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()