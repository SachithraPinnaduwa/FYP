from subject_90 import *

import unittest

def transform_array_after_operations(a, k):
    li = []
    for i in range(k):
        m = max(a)
        a = [m - i for i in a]
        if a in li:
            if not k % 2:
                return li[-1]
            return a
        li.append(a)
    return a

class TestTransformArrayAfterOperations(unittest.TestCase):
    def test_normal_case_1(self):
        self.assertEqual(transform_array_after_operations([1, 2, 3], 2), [2, 1, 0])

    def test_normal_case_2(self):
        self.assertEqual(transform_array_after_operations([-4, 0, -1, 0], 2), [0, 4, 3, 4])

    def test_normal_case_3(self):
        self.assertEqual(transform_array_after_operations([5], 3), [5])

    def test_normal_case_4(self):
        self.assertEqual(transform_array_after_operations([-1], 5), [-1])

    def test_normal_case_5(self):
        self.assertEqual(transform_array_after_operations([2, 2, 2], 4), [2, 2, 2])

    def test_normal_case_6(self):
        self.assertEqual(transform_array_after_operations([0, 1, 2], 100000), [1, 0, 1])

    def test_normal_case_7(self):
        self.assertEqual(transform_array_after_operations([], 0), [])

    def test_error_handling_1(self):
        with self.assertRaises(ValueError):
            transform_array_after_operations([1, 2, 3], -1)

    def test_error_handling_2(self):
        with self.assertRaises(ValueError):
            transform_array_after_operations([1, 2, 3], 100001)

    def test_normal_case_8(self):
        self.assertEqual(transform_array_after_operations([0], 2), [0])

    def test_boundary_values_1(self):
        self.assertEqual(transform_array_after_operations([1, 2, 3], 0), [1, 2, 3])

    def test_boundary_values_2(self):
        self.assertEqual(transform_array_after_operations([1, 2, 3], 100000), [1, 0, 1])

if __name__ == '__main__':
    unittest.main()