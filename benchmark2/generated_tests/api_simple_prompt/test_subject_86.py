from subject_86 import *

import unittest

def shortest_path(tree, source, destination):
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

    path, num_nodes = dfs(source, destination, [])

    if path is None:
        return "No path found between source and destination"

    return path, num_nodes

class TestShortestPath(unittest.TestCase):
    def test_shortest_path(self):
        tree = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }
        self.assertEqual(shortest_path(tree, 'A', 'F'), (['A', 'B', 'E', 'F'], 4))
        self.assertEqual(shortest_path(tree, 'A', 'D'), (['A', 'B', 'D'], 3))
        self.assertEqual(shortest_path(tree, 'A', 'A'), (['A'], 1))
        self.assertEqual(shortest_path(tree, 'A', 'Z'), "Source or destination node not found in the tree")
        self.assertEqual(shortest_path(tree, 'Z', 'A'), "Source or destination node not found in the tree")
        self.assertEqual(shortest_path(tree, 'A', 'B'), (['A', 'B'], 2))
        self.assertEqual(shortest_path(tree, 'A', 'C'), (['A', 'C'], 2))
        self.assertEqual(shortest_path(tree, 'A', 'E'), (['A', 'B', 'E'], 3))
        self.assertEqual(shortest_path(tree, 'B', 'F'), (['B', 'E', 'F'], 3))
        self.assertEqual(shortest_path(tree, 'C', 'F'), (['C', 'F'], 2))
        self.assertEqual(shortest_path(tree, 'D', 'F'), "No path found between source and destination")
        self.assertEqual(shortest_path(tree, 'E', 'D'), "No path found between source and destination")

if __name__ == '__main__':
    unittest.main()