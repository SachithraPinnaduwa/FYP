import unittest

class TestGraph(unittest.TestCase):
    def test_adjacency_matrix_to_list(self):
        # Test case 1: Basic graph
        matrix1 = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0]
        ]
        expected1 = {
            0: [1],
            1: [2],
            2: [0]
        }
        result1 = adjacency_matrix_to_list(matrix1)
        self.assertEqual(result1, expected1)

        # Test case 2: Graph with multiple edges
        matrix2 = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]
        expected2 = {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        }
        result2 = adjacency_matrix_to_list(matrix2)
        self.assertEqual(result2, expected2)

        # Test case 3: Graph with no edges
        matrix3 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        expected3 = {
            0: [],
            1: [],
            2: []
        }
        result3 = adjacency_matrix_to_list(matrix3)
        self.assertEqual(result3, expected3)

        # Test case 4: Graph with self-loops
        matrix4 = [
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 1]
        ]
        expected4 = {
            0: [0, 1],
            1: [0, 2],
            2: [1, 2]
        }
        result4 = adjacency_matrix_to_list(matrix4)
        self.assertEqual(result4, expected4)

if __name__ == '__main__':
    unittest.main()
