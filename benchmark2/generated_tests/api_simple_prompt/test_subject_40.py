from subject_40 import *

import unittest

def min_increment_operations(arr, N):
    c = 0
    arr.sort()
    for i in range(1, N):
        if arr[i] <= arr[i - 1]:
            c += arr[i - 1] + 1 - arr[i]
            arr[i] = arr[i - 1] + 1
    return c

class TestMinIncrementOperations(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(min_increment_operations([1, 2, 2], 3), 1)

    def test_case_2(self):
        self.assertEqual(min_increment_operations([1, 1, 2, 3], 4), 3)

    def test_case_3(self):
        self.assertEqual(min_increment_operations([1, 2, 3, 4], 4), 0)

    def test_case_4(self):
        self.assertEqual(min_increment_operations([5, 1, 3, 4, 2], 5), 0)

    def test_case_5(self):
        self.assertEqual(min_increment_operations([10, 10, 10, 10], 4), 12)

    def test_case_6(self):
        self.assertEqual(min_increment_operations([1, 1000000000, 1000000000, 1000000000], 4), 2999999997)

if __name__ == '__main__':
    unittest.main()