import unittest

class TestTopologicalSorter(unittest.TestCase):
    def setUp(self):
        self.sorter = TopologicalSorter()

    def test_add_edge(self):
        self.sorter.add_edge(1, 2)
        self.sorter.add_edge(2, 3)
        self.assertEqual(self.sorter.graph, {1: [2], 2: [3], 3: []})
        self.assertEqual(self.sorter.in_degree, {1: 0, 2: 1, 3: 1})

    def test_sort_simple(self):
        self.sorter.add_edge(1, 2)
        self.sorter.add_edge(2, 3)
        result = self.sorter.sort()
        self.assertEqual(result, [1, 2, 3])

    def test_sort_disconnected(self):
        self.sorter.add_edge(1, 2)
        self.sorter.add_edge(3, 4)
        result = self.sorter.sort()
        self.assertEqual(result, [1, 2, 3, 4] or [3, 4, 1, 2])

    def test_sort_cycle(self):
        self.sorter.add_edge(1, 2)
        self.sorter.add_edge(2, 3)
        self.sorter.add_edge(3, 1)
        with self.assertRaises(ValueError):
            self.sorter.sort()

    def test_sort_single_node(self):
        self.sorter.add_edge(1, 1)
        with self.assertRaises(ValueError):
            self.sorter.sort()

    def test_sort_empty_graph(self):
        result = self.sorter.sort()
        self.assertEqual(result, [])

    def test_sort_complex(self):
        self.sorter.add_edge(1, 2)
        self.sorter.add_edge(1, 3)
        self.sorter.add_edge(2, 4)
        self.sorter.add_edge(3, 4)
        result = self.sorter.sort()
        self.assertEqual(result, [1, 2, 3, 4] or [1, 3, 2, 4])

if __name__ == '__main__':
    unittest.main()
