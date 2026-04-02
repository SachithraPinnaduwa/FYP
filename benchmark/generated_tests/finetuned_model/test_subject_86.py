import unittest

def shortest_path(tree, source, destination):
    # Check if both the source and destination nodes are present in the tree
    if source not in tree or destination not in tree:
        return "Source or destination node not found in the tree"

    visited = []

    def dfs(node, dest, path):
        visited.append(node)
        if node == dest:
            return path + [node], len(visited)

        for neighbor in tree[node]:
            if neighbor not in visited:
                new_path, num_nodes = dfs(neighbor, dest, path + [node])
                if new_path is not None:
                    return new_path, num_nodes

        return None, len(visited)

    # Call the helper function with source and destination nodes as arguments
    path, num_nodes = dfs(source, destination, [])

    # If no path was found, return an error message
    if path is None:
        return "No path found between source and destination"

    return path, num_nodes

class TestShortestPath(unittest.TestCase):
    def test_basic_path(self):
        tree = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['D'],
            'D': []
        }
        self.assertEqual(shortest_path(tree, 'A', 'D'), (['A', 'B', 'D'], 3))

    def test_path_with_one_node(self):
        tree = {
            'A': []
        }
        self.assertEqual(shortest_path(tree, 'A', 'A'), (['A'], 1))

    def test_missing_source_node(self):
        tree = {
            'A': ['B'],
            'B': []
        }
        self.assertEqual(shortest_path(tree, 'C', 'A'), "Source or destination node not found in the tree")

    def test_missing_destination_node(self):
        tree = {
            'A': ['B'],
            'B': []
        }
        self.assertEqual(shortest_path(tree, 'A', 'C'), "Source or destination node not found in the tree")

    def test_no_path(self):
        tree = {
            'A': ['B'],
            'B': []
        }
        self.assertEqual(shortest_path(tree, 'A', 'C'), "No path found between source and destination")

    def test_cyclical_dependency(self):
        tree = {
            'A': ['B'],
            'B': ['C'],
            'C': ['A']
        }
        self.assertEqual(shortest_path(tree, 'A', 'C'), "No path found between source and destination")

    def test_large_tree(self):
        tree = {str(i): [str(i+1)] for i in range(1000000)}  # Tree with 1,000,000 nodes
        self.assertEqual(shortest_path(tree, '0', '999999'), (['0', '1', '2', '3', '4', '5', '6', '7', '8', '999999'], 10))

    def test_single_node_tree(self):
        tree = {
            'A': []
        }
        self.assertEqual(shortest_path(tree, 'A', 'A'), (['A'], 1))

    def test_two_node_tree(self):
        tree = {
            'A': ['B'],
            'B': []
        }
        self.assertEqual(shortest_path(tree, 'A', 'B'), (['A', 'B'], 2))

    def test_path_with_two_nodes(self):
        tree = {
            'A': ['B'],
            'B': []
        }
        self.assertEqual(shortest_path(tree, 'A', 'B'), (['A', 'B'], 2))

    def test_path_with_multiple_neighbors(self):
        tree = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['D', 'E'],
            'D': [],
            'E': []
        }
        self.assertEqual(shortest_path(tree, 'A', 'D'), (['A', 'B', 'D'], 3))
        self.assertEqual(shortest_path(tree, 'A', 'E'), (['A', 'C', 'E'], 3))

    def test_path_with_multiple_paths(self):
        tree = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['D', 'E'],
            'D': [],
            'E': []
        }
        self.assertEqual(shortest_path(tree, 'A', 'D'), (['A', 'B', 'D'], 3))
        self.assertEqual(shortest_path(tree, 'A', 'E'), (['A', 'C', 'E'], 3))

    def test_path_with_large_number_of_nodes(self):
        tree = {str(i): [str(i+1)] for i in range(1000000)}  # Tree with 1,000,000 nodes
        self.assertEqual(shortest_path(tree, '0', '999999'), (['0', '1', '2', '3', '4', '5', '6', '7', '8', '999999'], 10))

    def test_path_with_single_node(self):
        tree = {
            'A': []
        }
        self.assertEqual(shortest_path(tree, 'A', 'A'), (['A'], 1))

    def test_path_with_single_node_tree(self):
        tree = {
            'A': []
        }
        self.assertEqual(shortest_path(tree, 'A', 'A'), (['A'], 1))

if __name__ == '__main__':
    unittest.main()