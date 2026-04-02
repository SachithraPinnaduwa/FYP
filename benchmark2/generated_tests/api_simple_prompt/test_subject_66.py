from subject_66 import *

import unittest

def entrance(N):
    diagonal_sums = []
    for _ in range(N):
        matrix = [[(i * 110 + j) % 200 - 100 for j in range(4)] for i in range(4)]
        diagonal_sum = sum(matrix[i][i] for i in range(4))
        diagonal_sums.append(diagonal_sum)
    return diagonal_sums

class TestEntranceFunction(unittest.TestCase):
    def test_single_matrix(self):
        N = 1
        expected = [0]
        self.assertEqual(entrance(N), expected)

    def test_multiple_matrices(self):
        N = 3
        expected = [0, 0, 0]
        self.assertEqual(entrance(N), expected)

    def test_large_N(self):
        N = 1000000
        expected = [0] * N
        self.assertEqual(entrance(N), expected)

    def test_negative_values(self):
        N = 1
        expected = [-100]
        self.assertEqual(entrance(N), expected)

    def test_positive_values(self):
        N = 1
        expected = [100]
        self.assertEqual(entrance(N), expected)

    def test_random_values(self):
        N = 1
        expected = [0]
        self.assertEqual(entrance(N), expected)

if __name__ == '__main__':
    unittest.main()