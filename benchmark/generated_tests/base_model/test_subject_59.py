import unittest

class TestAdjacencyMatrixToList(unittest.TestCase):

    def test_empty_matrix(self):
        self.assertEqual(adjacency_matrix_to_list([]), {})

    def test_single_node_graph(self):
        self.assertEqual(adjacency_matrix_to_list([[0]]), {0: []})

    def test_two_nodes_no_edge(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 0], [0, 0]]), {0: [], 1: []})

    def test_two_nodes_with_edge(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 1], [1, 0]]), {0: [1], 1: [0]})

    def test_three_nodes_complete_graph(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 1, 1], [1, 0, 1], [1, 1, 0]]), {0: [1, 2], 1: [0, 2], 2: [0, 1]})

    def test_four_nodes_disconnected(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]), {0: [], 1: [], 2: [], 3: []})

    def test_four_nodes_one_connected_component(self):
        self.assertEqual(adjacency_matrix_to_list([[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]]), {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: []})

if __name__ == '__main__':
    unittest.main()