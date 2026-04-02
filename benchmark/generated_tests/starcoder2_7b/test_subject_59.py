import unittest

class TestAdjacencyMatrixToList(unittest.TestCase):
    def test_adjacency_matrix_to_list(self):
        matrix = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
        expected_output = {0: [1, 3], 1: [0, 2, 3], 2: [1, 3], 3: [0, 1, 2]}
        self.assertEqual(adjacency_matrix_to_list(matrix), expected_output)

if __name__ == '__main__':
    unittest.main()