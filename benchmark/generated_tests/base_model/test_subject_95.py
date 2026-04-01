import unittest

class TestMinimumCostArborescence(unittest.TestCase):

    def test_case_1(self):
        num_vertices = 4
        num_edges = 6
        root = 0
        edges = [
            (0, 1, 3),
            (0, 2, 2),
            (2, 0, 1),
            (2, 3, 1),
            (3, 0, 1),
            (3, 1, 5)
        ]
        expected_output = 6
        self.assertEqual(minimum_cost_arborescence(num_vertices, num_edges, root, edges), expected_output)

    def test_case_2(self):
        num_vertices = 6
        num_edges = 10
        root = 0
        edges = [
            (0, 2, 7),
            (0, 1, 1),
            (0, 3, 5),
            (1, 4, 9),
            (2, 1, 6),
            (1, 3, 2),
            (3, 4, 3),
            (4, 2, 2),
            (2, 5, 8),
            (3, 5, 3)
        ]
        expected_output = 11
        self.assertEqual(minimum_cost_arborescence(num_vertices, num_edges, root, edges), expected_output)

    def test_case_3(self):
        num_vertices = 5
        num_edges = 4
        root = 0
        edges = [
            (0, 1, 2),
            (0, 2, 3),
            (1, 3, 1),
            (2, 4, 4)
        ]
        expected_output = 6
        self.assertEqual(minimum_cost_arborescence(num_vertices, num_edges, root, edges), expected_output)

    def test_case_4(self):
        num_vertices = 3
        num_edges = 3
        root = 1
        edges = [
            (0, 1, 5),
            (1, 2, 2),
            (2, 0, 3)
        ]
        expected_output = 7
        self.assertEqual(minimum_cost_arborescence(num_vertices, num_edges, root, edges), expected_output)

if __name__ == '__main__':
    unittest.main()