import unittest

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge(0, 1, 4)
        self.graph.add_edge(0, 2, 2)
        self.graph.add_edge(1, 2, 1)
        self.graph.add_edge(2, 3, 5)
        self.graph.add_edge(3, 1, 8)
        self.graph.add_edge(3, 4, 2)
        self.graph.add_edge(4, 1, 6)

    def test_shortest_path(self):
        self.assertEqual(self.graph.shortest_path(0, 4), 7)
        self.assertEqual(self.graph.shortest_path(0, 3), 7)
        self.assertEqual(self.graph.shortest_path(0, 1), 4)
        self.assertEqual(self.graph.shortest_path(0, 2), 2)
        self.assertEqual(self.graph.shortest_path(0, 0), 0)
        self.assertEqual(self.graph.shortest_path(0, 5), float("inf"))

if __name__ == "__main__":
    unittest.main()
