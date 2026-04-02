from subject_66 import *

import unittest
import random

def entrance(N):
    diagonal_sums = []
    for _ in range(N):
        matrix = [[(i * 110 + j) % 200 - 100 for j in range(4)] for i in range(4)]
        diagonal_sum = sum(matrix[i][i] for i in range(4))
        diagonal_sums.append(diagonal_sum)
    return diagonal_sums

class TestEntranceFunction(unittest.TestCase):
    def test_normal_case(self):
        N = 5
        result = entrance(N)
        self.assertEqual(len(result), N)
        for diagonal_sum in result:
            self.assertIsInstance(diagonal_sum, int)

    def test_edge_case_min(self):
        N = 1
        result = entrance(N)
        self.assertEqual(len(result), N)
        for diagonal_sum in result:
            self.assertIsInstance(diagonal_sum, int)

    def test_edge_case_max(self):
        N = 10**6
        result = entrance(N)
        self.assertEqual(len(result), N)
        for diagonal_sum in result:
            self.assertIsInstance(diagonal_sum, int)

    def test_error_handling_non_integer(self):
        N = '5'
        with self.assertRaises(TypeError):
            entrance(N)

    def test_error_handling_negative(self):
        N = -5
        with self.assertRaises(ValueError):
            entrance(N)

if __name__ == '__main__':
    unittest.main()