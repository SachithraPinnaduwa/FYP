from subject_86 import *

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
    def test_normal_case(self):
        tree = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        source = 'A'
        destination = 'D'
        expected_path = ['A', 'B', 'D']
        expected_num_nodes = 3
        self.assertEqual(shortest_path(tree, source, destination), (expected_path, expected_num_nodes))

    def test_edge_case_single_node(self):
        tree = {'A': []}
        source = 'A'
        destination = 'A'
        expected_path = ['A']
        expected_num_nodes = 1
        self.assertEqual(shortest_path(tree, source, destination), (expected_path, expected_num_nodes))

    def test_error_handling_missing_source_node(self):
        tree = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        source = 'E'
        destination = 'D'
        expected_message = 'Source or destination node not found in the tree'
        self.assertEqual(shortest_path(tree, source, destination), expected_message)

    def test_error_handling_missing_destination_node(self):
        tree = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        source = 'A'
        destination = 'E'
        expected_message = 'Source or destination node not found in the tree'
        self.assertEqual(shortest_path(tree, source, destination), expected_message)

    def test_error_handling_cyclical_dependency(self):
        tree = {'A': ['B'], 'B': ['A']}
        source = 'A'
        destination = 'B'
        expected_message = 'No path found between source and destination'
        self.assertEqual(shortest_path(tree, source, destination), expected_message)

if __name__ == '__main__':
    unittest.main()