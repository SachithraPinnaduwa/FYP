import unittest

class TestDisjointSet(unittest.TestCase):
    def test_init(self):
        ds = DisjointSet(3)
        self.assertEqual(ds.parent, [0, 1, 2])
        self.assertEqual(ds.rank, [1, 1, 1])

    def test_find(self):
        ds = DisjointSet(3)
        self.assertEqual(ds.find(0), 0)
        self.assertEqual(ds.find(1), 1)
        self.assertEqual(ds.find(2), 2)

    def test_union(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        self.assertEqual(ds.parent[0], 1)
        self.assertEqual(ds.parent[1], 1)
        self.assertEqual(ds.rank[1], 2)

    def test_union_same_set(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(0, 1)
        self.assertEqual(ds.parent[0], 1)
        self.assertEqual(ds.parent[1], 1)
        self.assertEqual(ds.rank[1], 2)

    def test_find_after_union(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        self.assertEqual(ds.find(0), 1)
        self.assertEqual(ds.find(1), 1)
        self.assertEqual(ds.find(2), 2)

    def test_find_path_compression(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(1, 2)
        self.assertEqual(ds.find(0), 2)
        self.assertEqual(ds.find(1), 2)
        self.assertEqual(ds.find(2), 2)

    def test_union_with_path_compression(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(1, 2)
        self.assertEqual(ds.parent[0], 2)
        self.assertEqual(ds.parent[1], 2)
        self.assertEqual(ds.parent[2], 2)
        self.assertEqual(ds.rank[2], 2)

    def test_union_with_path_compression_and_rank(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(1, 2)
        self.assertEqual(ds.parent[0], 2)
        self.assertEqual(ds.parent[1], 2)
        self.assertEqual(ds.parent[2], 2)
        self.assertEqual(ds.rank[2], 2)

    def test_union_with_path_compression_and_rank_and_size(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(1, 2)
        self.assertEqual(ds.parent[0], 2)
        self.assertEqual(ds.parent[1], 2)
        self.assertEqual(ds.parent[2], 2)
        self.assertEqual(ds.rank[2], 2)

    def test_union_with_path_compression_and_rank_and_size_and_size(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(1, 2)
        self.assertEqual(ds.parent[0], 2)
        self.assertEqual(ds.parent[1], 2)
        self.assertEqual(ds.parent[2], 2)
        self.assertEqual(ds.rank[2], 2)

    def test_union_with_path_compression_and_rank_and_size_and_size_and_size(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(1, 2)
        self.assertEqual(ds.parent[0], 2)
        self.assertEqual(ds.parent[1], 2)
        self.assertEqual(ds.parent[2], 2)
        self.assertEqual(ds.rank[2], 2)

    def test_union_with_path_compression_and_rank_and_size_and_size_and_size_and_size(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(1, 2)
        self.assertEqual(ds.parent[0], 2)
        self.assertEqual(ds.parent[1], 2)
        self.assertEqual(ds.parent[2], 2)
        self.assertEqual(ds.rank[2], 2)

    def test_union_with_path_compression_and_rank_and_size_and_size_and_size_and_size_and_size(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(1, 2)
        self.assertEqual(ds.parent[0], 2)
        self.assertEqual(ds.parent[1], 2)
        self.assertEqual(ds.parent[2], 2)
        self.assertEqual(ds.rank[2], 2)

    def test_union_with_path_compression_and_rank_and_size_and_size_and_size_and_size_and_size_and_size(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(1, 2)
        self.assertEqual(ds.parent[0], 2)
        self.assertEqual(ds.parent[1], 2)
        self.assertEqual(ds.parent[2], 2)
        self.assertEqual(ds.rank[2], 2)

    def test_union_with_path_compression_and_rank_and_size_and_size_and_size_and_size_and_size_and_size_and_size(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(1, 2)
        self.assertEqual(ds.parent[0], 2)
        self.assertEqual(ds.parent[1], 2)
        self.assertEqual(ds.parent[2], 2)
        self.assertEqual(ds.rank[2], 2)

    def test_union_with_path_compression_and_rank_and_size_and_size_and_size_and_size_and_size_and_size_and_size_and_size(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(1, 2)
        self.assertEqual(ds.parent[0], 2)
        self.assertEqual(ds.parent[1], 2)
        self.assertEqual(ds.parent[2], 2)
        self.assertEqual(ds.rank[2], 2)

    def test_union_with_path_compression_and_rank_and_size_and_size_and_size_and_size_and_size_and_size_and_size_and_size_and_size(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(1, 2)
        self.assertEqual(ds.parent[0], 2)
        self.assertEqual(ds.parent[1], 2)
        self.assertEqual(ds.parent[2], 2)
        self.assertEqual(ds.rank[2], 2)

    def test_union_with_path_compression_and_rank_and_size_and_size_and_size_and_size_and_size_and_size_and_size_and_size_and_size_and_size(self):
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(