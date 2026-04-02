from subject_93 import *

import unittest

def count_valid_and_pairs(A):
    N = len(A)
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] & A[j] == A[i]:
                count += 1
    return count

class TestCountValidAndPairs(unittest.TestCase):
    def test_normal_case_1(self):
        A = [1, 1, 1, 1, 1]
        expected = 10
        self.assertEqual(count_valid_and_pairs(A), expected)

    def test_normal_case_2(self):
        A = [1, 2, 3, 4, 5]
        expected = 4
        self.assertEqual(count_valid_and_pairs(A), expected)

    def test_normal_case_3(self):
        A = [10, 10, 10, 10]
        expected = 6
        self.assertEqual(count_valid_and_pairs(A), expected)

    def test_normal_case_4(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = 20
        self.assertEqual(count_valid_and_pairs(A), expected)

    def test_edge_case_1(self):
        A = [1]
        expected = 0
        self.assertEqual(count_valid_and_pairs(A), expected)

    def test_edge_case_2(self):
        A = [1] * 100
        expected = 4950
        self.assertEqual(count_valid_and_pairs(A), expected)

    def test_error_handling_1(self):
        A = []
        expected = 0
        self.assertEqual(count_valid_and_pairs(A), expected)

    def test_error_handling_2(self):
        A = [-1, -2, -3]
        expected = 0
        self.assertEqual(count_valid_and_pairs(A), expected)

    def test_error_handling_3(self):
        A = [101, 102, 103]
        expected = 0
        self.assertEqual(count_valid_and_pairs(A), expected)

if __name__ == '__main__':
    unittest.main()