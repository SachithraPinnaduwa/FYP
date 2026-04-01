import unittest

class TestShortestPath(unittest.TestCase):

    def test_shortest_path_exists(self):
        tree = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }
        self.assertEqual(shortest_path(tree, 'A', 'F'), (['A', 'B', 'E', 'F'], 4))

    def test_shortest_path_no_path(self):
        tree = {
            'A': ['B'],
            'B': ['C'],
            'C': ['D']
        }
        self.assertEqual(shortest_path(tree, 'A', 'D'), "No path found between source and destination")

    def test_missing_source_node(self):
        tree = {
            'A': ['B'],
            'B': ['C'],
            'C': ['D']
        }
        self.assertEqual(shortest_path(tree, 'X', 'D'), "Source or destination node not found in the tree")

    def test_missing_destination_node(self):
        tree = {
            'A': ['B'],
            'B': ['C'],
            'C': ['D']
        }
        self.assertEqual(shortest_path(tree, 'A', 'Z'), "Source or destination node not found in the tree")

    def test_cyclical_dependency(self):
        tree = {
            'A': ['B'],
            'B': ['A']
        }
        self.assertEqual(shortest_path(tree, 'A', 'B'), "No path found between source and destination")

    def test_single_node_tree(self):
        tree = {'A': []}
        self.assertEqual(shortest_path(tree, 'A', 'A'), (['A'], 1))

if __name__ == '__main__':
    unittest.main()