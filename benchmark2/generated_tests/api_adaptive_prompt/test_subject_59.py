from subject_59 import *

import unittest

def adjacency_matrix_to_list(matrix):
    adj_list = {}
    for i in range(len(matrix)):
        adj_list[i] = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adj_list[i].append(j)
    return adj_list

class TestAdjacencyMatrixToList(unittest.TestCase):
    def test_normal_case_1(self):
        matrix = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        expected = {0: [1], 1: [0, 2], 2: [1]}
        self.assertEqual(adjacency_matrix_to_list(matrix), expected)

    def test_normal_case_2(self):
        matrix = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
        expected = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]}
        self.assertEqual(adjacency_matrix_to_list(matrix), expected)

    def test_normal_case_3(self):
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = {0: [], 1: [], 2: []}
        self.assertEqual(adjacency_matrix_to_list(matrix), expected)

    def test_edge_case_1(self):
        matrix = [[]]
        expected = {}
        self.assertEqual(adjacency_matrix_to_list(matrix), expected)

    def test_error_handling_1(self):
        matrix = [[0, 1], [1, 0], [0, 0]]
        with self.assertRaises(ValueError):
            adjacency_matrix_to_list(matrix)

    def test_error_handling_2(self):
        matrix = [[0, 1, 0], [1, '0', 1], [0, 1, 0]]
        with self.assertRaises(TypeError):
            adjacency_matrix_to_list(matrix)

if __name__ == '__main__':
    unittest.main()