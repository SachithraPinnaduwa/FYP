import unittest

class TestMinimumCostArborescence(unittest.TestCase):

    # Test case for the example given in the problem description
    def test_example1(self):
        num_vertices = 4
        num_edges = 6
        root = 0
        edges = [(0, 1, 3), (0, 2, 2), (2, 0, 1), (2, 3, 1), (3, 0, 1), (3, 1, 5)]
        self.assertEqual(minimum_cost_arborescence(num_vertices, num_edges, root, edges), 6)

    # Test case for another example given in the problem description
    def test_example2(self):
        num_vertices = 6
        num_edges = 10
        root = 0
        edges = [(0, 2, 7), (0, 1, 1), (0, 3, 5), (1, 4, 9), (2, 1, 6), (1, 3, 2), (3, 4, 3), (4, 2, 2), (2, 5, 8), (3, 5, 3)]
        self.assertEqual(minimum_cost_arborescence(num_vertices, num_edges, root, edges), 11)

    # Test case for a graph with only one vertex
    def test_single_vertex(self):
        num_vertices = 1
        num_edges = 0
        root = 0
        edges = []
        self.assertEqual(minimum_cost_arborescence(num_vertices, num_edges, root, edges), 0)

    # Test case for a graph with two vertices
    def test_two_vertices(self):
        num_vertices = 2
        num_edges = 1
        root = 0
        edges = [(0, 1, 10)]
        self.assertEqual(minimum_cost_arborescence(num_vertices, num_edges, root, edges), 10)

    # Test case for a graph with three vertices and no edges
    def test_no_edges(self):
        num_vertices = 3
        num_edges = 0
        root = 0
        edges = []
        self.assertEqual(minimum_cost_arborescence(num_vertices, num_edges, root, edges), 0)

    # Test case for a graph with a cycle
    def test_cycle(self):
        num_vertices = 4
        num_edges = 4
        root = 0
        edges = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 0, 4)]
        self.assertEqual(minimum_cost_arborescence(num_vertices, num_edges, root, edges), 6)