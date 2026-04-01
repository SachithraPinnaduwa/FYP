import unittest

class TestShortestPathFunction(unittest.TestCase):
    def test_source_destination_in_tree(self):
        # Test case where source and destination nodes are present in the tree
        tree = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['E'],
            'D': [],
            'E': []
        }
        source = 'A'
        destination = 'E'
        self.assertEqual(shortest_path(tree, source, destination), (['A', 'C', 'E'], 3))

    def test_source_not_in_tree(self):
        # Test case where source node is not present in the tree
        tree = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['E'],
            'D': [],
            'E': []
        }
        source = 'F'
        destination = 'E'
        self.assertEqual(shortest_path(tree, source, destination), "Source or destination node not found in the tree")

    def test_destination_not_in_tree(self):
        # Test case where destination node is not present in the tree
        tree = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['E'],
            'D': [],
            'E': []
        }
        source = 'A'
        destination = 'F'
        self.assertEqual(shortest_path(tree, source, destination), "Source or destination node not found in the tree")

    def test_cyclical_dependency(self):
        # Test case with cyclical dependency
        tree = {
            'A': ['B'],
            'B': ['C'],
            'C': ['A']
        }
        source = 'A'
        destination = 'C'
        self.assertEqual(shortest_path(tree, source, destination), (['A', 'B', 'C'], 3))

    def test_no_path(self):
        # Test case with no path
        tree = {
            'A': ['B'],
            'B': []
        }
        source = 'A'
        destination = 'B'
        self.assertEqual(shortest_path(tree, source, destination), "No path found between source and destination")

    def test_single_node_tree(self):
        # Test case with a single node tree
        tree = {
            'A': []
        }
        source = 'A'
        destination = 'A'
        self.assertEqual(shortest_path(tree, source, destination), (['A'], 1))

    def test_single_node_tree_no_path(self):
        # Test case with a single node tree and no path
        tree = {
            'A': []
        }
        source = 'A'
        destination = 'B'
        self.assertEqual(shortest_path(tree, source, destination), "Source or destination node not found in the tree")