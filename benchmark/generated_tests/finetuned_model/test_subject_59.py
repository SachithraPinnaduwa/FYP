import unittest

class TestAdjacencyMatrixToList(unittest.TestCase):

    def test_empty_matrix(self):
        # Test case for an empty matrix (0 nodes)
        matrix = []
        expected_output = {}
        self.assertEqual(adjacency_matrix_to_list(matrix), expected_output)

    def test_single_node(self):
        # Test case for a matrix with a single node
        matrix = [[0]]
        expected_output = {0: []}
        self.assertEqual(adjacency_matrix_to_list(matrix), expected_output)

    def test_two_nodes_no_edge(self):
        # Test case for a matrix with two nodes and no edge
        matrix = [[0, 0], [0, 0]]
        expected_output = {0: [], 1: []}
        self.assertEqual(adjacency_matrix_to_list(matrix), expected_output)

    def test_two_nodes_with_edge(self):
        # Test case for a matrix with two nodes and an edge
        matrix = [[0, 1], [1, 0]]
        expected_output = {0: [1], 1: [0]}
        self.assertEqual(adjacency_matrix_to_list(matrix), expected_output)

    def test_three_nodes(self):
        # Test case for a matrix with three nodes
        matrix = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        expected_output = {0: [1], 1: [0, 2], 2: [1]}
        self.assertEqual(adjacency_matrix_to_list(matrix), expected_output)

    def test_complete_graph(self):
        # Test case for a complete graph (all nodes are connected)
        n = 3
        matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        expected_output = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
        self.assertEqual(adjacency_matrix_to_list(matrix), expected_output)

    def test_disconnected_graph(self):
        # Test case for a disconnected graph (two separate components)
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected_output = {0: [], 1: [], 2: []}
        self.assertEqual(adjacency_matrix_to_list(matrix), expected_output)

    def test_large_graph(self):
        # Test case for a large graph (10 nodes)
        n = 10
        matrix = [[0]*n for _ in range(n)]
        matrix[0][1] = matrix[1][0] = 1
        matrix[2][3] = matrix[3][2] = 1
        matrix[4][5] = matrix[5][4] = 1
        matrix[6][7] = matrix[7][6] = 1
        matrix[8][9] = matrix[9][8] = 1
        expected_output = {0: [1], 1: [0], 2: [3], 3: [2], 4: [5], 5: [4], 6: [7], 7: [6], 8: [9], 9: [8]}
        self.assertEqual(adjacency_matrix_to_list(matrix), expected_output)