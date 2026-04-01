import unittest

class TestTransformArrayAfterOperations(unittest.TestCase):

    def test_transform_array_after_operations(self):
        self.assertEqual(transform_array_after_operations([-4, 0, -1, 0], 2), [0, 4, 3, 4])
        self.assertEqual(transform_array_after_operations([0, -1, 0, 0, -1, -1, -1, -1, 1, -1], 1), [1, 2, 1, 1, 2, 2, 2, 2, 0, 2])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 1), [4, 3, 2, 1, 0])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 2), [3, 2, 1, 0, 4])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 3), [2, 1, 0, 4, 3])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 4), [1, 0, 4, 3, 2])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 5), [0, 4, 3, 2, 1])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 6), [4, 3, 2, 1, 0])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 7), [3, 2, 1, 0, 4])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 8), [2, 1, 0, 4, 3])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 9), [1, 0, 4, 3, 2])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 10), [0, 4, 3, 2, 1])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 11), [4, 3, 2, 1, 0])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 12), [3, 2, 1, 0, 4])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 13), [2, 1, 0, 4, 3])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 14), [1, 0, 4, 3, 2])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 15), [0, 4, 3, 2, 1])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 16), [4, 3, 2, 1, 0])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 17), [3, 2, 1, 0, 4])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 18), [2, 1, 0, 4, 3])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 19), [1, 0, 4, 3, 2])
        self.assertEqual(transform_array_after_operations([1, 2, 3, 4, 5], 20), [0, 4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()