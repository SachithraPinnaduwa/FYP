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
    def test_empty_matrix(self):
        self.assertEqual(adjacency_matrix_to_list([]), {})

    def test_single_node(self):
        self.assertEqual(adjacency_matrix_to_list([[0]]), {0: []})

    def test_two_nodes_no_edge(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 0], [0, 0]]), {0: [], 1: []})

    def test_two_nodes_with_edge(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 1], [1, 0]]), {0: [1], 1: [0]})

    def test_three_nodes_no_edges(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), {0: [], 1: [], 2: []})

    def test_three_nodes_with_edges(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 1, 0], [1, 0, 1], [0, 1, 0]]), {0: [1], 1: [0, 2], 2: [1]})

    def test_four_nodes_no_edges(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]), {0: [], 1: [], 2: [], 3: []})

    def test_four_nodes_with_edges(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]), {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})

if __name__ == '__main__':
    unittest.main()