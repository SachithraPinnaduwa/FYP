import unittest

class TestDependencyGraph(unittest.TestCase):
    def setUp(self):
        self.graph = DependencyGraph()

    def test_add_node(self):
        self.graph.add_node("A")
        self.graph.add_node("B")
        self.assertEqual(self.graph.graph.keys(), {"A", "B"})

    def test_add_dependency(self):
        self.graph.add_node("A")
        self.graph.add_node("B")
        self.graph.add_dependency("A", "B")
        self.assertEqual(self.graph.graph["A"], ["B"])

    def test_resolve(self):
        self.graph.add_node("A")
        self.graph.add_node("B")
        self.graph.add_dependency("A", "B")
        result = self.graph.resolve("A")
        self.assertEqual(result, ["B", "A"])

    def test_resolve_circular(self):
        self.graph.add_node("A")
        self.graph.add_node("B")
        self.graph.add_dependency("A", "B")
        self.graph.add_dependency("B", "A")
        with self.assertRaises(ValueError):
            self.graph.resolve("A")

if __name__ == "__main__":
    unittest.main()
