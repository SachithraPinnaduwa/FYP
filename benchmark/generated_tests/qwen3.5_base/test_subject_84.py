import unittest

class TestWeightedGraph(unittest.TestCase):
    def test_add_edge(self):
        graph = WeightedGraph()
        graph.add_edge('A', 'B', 1)
        graph.add_edge('B', 'C', 2)
        self.assertEqual(graph.vertices, {'A', 'B', 'C'})
        self.assertEqual(graph.edges, [(1, 'A', 'B'), (2, 'B', 'C')])

    def test_get_mst_kruskal(self):
        graph = WeightedGraph()
        graph.add_edge('A', 'B', 1)
        graph.add_edge('B', 'C', 2)
        graph.add_edge('A', 'C', 3)
        mst = graph.get_mst_kruskal()
        self.assertEqual(mst, [('A', 'B', 1), ('B', 'C', 2)])

    def test_get_mst_kruskal_empty(self):
        graph = WeightedGraph()
        mst = graph.get_mst_kruskal()
        self.assertEqual(mst, [])

    def test_get_mst_kruskal_single_edge(self):
        graph = WeightedGraph()
        graph.add_edge('A', 'B', 1)
        mst = graph.get_mst_kruskal()
        self.assertEqual(mst, [('A', 'B', 1)])

    def test_get_mst_kruskal_disconnected(self):
        graph = WeightedGraph()
        graph.add_edge('A', 'B', 1)
        graph.add_edge('C', 'D', 2)
        mst = graph.get_mst_kruskal()
        self.assertEqual(mst, [('A', 'B', 1), ('C', 'D', 2)])

if __name__ == '__main__':
    unittest.main()
