import unittest

class TestShortestPath(unittest.TestCase):
    def test_shortest_path(self):
        tree = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['D'],
            'D': []
        }
        source = 'A'
        destination = 'D'
        path, num_nodes = shortest_path(tree, source, destination)
        self.assertEqual(path, ['A', 'B', 'D'], "Path should be ['A', 'B', 'D']")
        self.assertEqual(num_nodes, 3, "Number of nodes should be 3")

    def test_shortest_path_with_multiple_paths(self):
        tree = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['D'],
            'D': []
        }
        source = 'A'
        destination = 'D'
        path, num_nodes = shortest_path(tree, source, destination)
        self.assertEqual(path, ['A', 'B', 'D'], "Path should be ['A', 'B', 'D']")
        self.assertEqual(num_nodes, 3, "Number of nodes should be 3")

    def test_shortest_path_with_no_path(self):
        tree = {
            'A': ['B'],
            'B': ['C'],
            'C': []
        }
        source = 'A'
        destination = 'D'
        path, num_nodes = shortest_path(tree, source, destination)
        self.assertEqual(path, "No path found between source and destination", "Path should be 'No path found between source and destination'")
        self.assertEqual(num_nodes, 0, "Number of nodes should be 0")

    def test_shortest_path_with_source_not_found(self):
        tree = {
            'A': ['B'],
            'B': ['C'],
            'C': []
        }
        source = 'D'
        destination = 'C'
        path, num_nodes = shortest_path(tree, source, destination)
        self.assertEqual(path, "Source or destination node not found in the tree", "Path should be 'Source or destination node not found in the tree'")
        self.assertEqual(num_nodes, 0, "Number of nodes should be 0")

    def test_shortest_path_with_destination_not_found(self):
        tree = {
            'A': ['B'],
            'B': ['C'],
            'C': []
        }
        source = 'A'
        destination = 'D'
        path, num_nodes = shortest_path(tree, source, destination)
        self.assertEqual(path, "Source or destination node not found in the tree", "Path should be 'Source or destination node not found in the tree'")
        self.assertEqual(num_nodes, 0, "Number of nodes should be 0")

    def test_shortest_path_with_single_node(self):
        tree = {
            'A': []
        }
        source = 'A'
        destination = 'A'
        path, num_nodes = shortest_path(tree, source, destination)
        self.assertEqual(path, ['A'], "Path should be ['A']")
        self.assertEqual(num_nodes, 1, "Number of nodes should be 1")

if __name__ == '__main__':
    unittest.main()
