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

    def test_single_node_matrix(self):
        self.assertEqual(adjacency_matrix_to_list([[0]]), {0: []})

    def test_single_edge_matrix(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 1], [1, 0]]), {0: [1], 1: [0]})

    def test_triangle_matrix(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 1, 1], [1, 0, 1], [1, 1, 0]]), {0: [1, 2], 1: [0, 2], 2: [0, 1]})

    def test_disconnected_matrix(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), {0: [], 1: [], 2: []})

    def test_complete_graph_matrix(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]), {0: [1, 2, 3], 1: [0, 2, 3], 2: [0, 1, 3], 3: [0, 1, 2]})

    def test_single_node_with_no_edges_matrix(self):
        self.assertEqual(adjacency_matrix_to_list([[0]]), {0: []})

    def test_single_node_with_self_edge_matrix(self):
        self.assertEqual(adjacency_matrix_to_list([[1]]), {0: [0]})

    def test_two_nodes_with_self_edges_matrix(self):
        self.assertEqual(adjacency_matrix_to_list([[1, 0], [0, 1]]), {0: [0], 1: [1]})

    def test_two_nodes_with_edge_between_them_matrix(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 1], [1, 0]]), {0: [1], 1: [0]})

    def test_three_nodes_with_edges_among_all_matrix(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 1, 1], [1, 0, 1], [1, 1, 0]]), {0: [1, 2], 1: [0, 2], 2: [0, 1]})

if __name__ == '__main__':
    unittest.main()