import unittest

class TestQuadTree(unittest.TestCase):
    def setUp(self):
        self.quad_tree = QuadTree()

    def test_insert_single_point(self):
        point = QuadTreePoint(1.0, 1.0, "test")
        self.assertTrue(self.quad_tree.insert(point))
        self.assertEqual(len(self.quad_tree.root.points), 1)

    def test_insert_multiple_points(self):
        points = [
            QuadTreePoint(1.0, 1.0, "a"),
            QuadTreePoint(2.0, 2.0, "b"),
            QuadTreePoint(3.0, 3.0, "c"),
            QuadTreePoint(4.0, 4.0, "d"),
        ]
        for point in points:
            self.assertTrue(self.quad_tree.insert(point))
        self.assertEqual(len(self.quad_tree.root.points), 4)

    def test_insert_outside_bounds(self):
        point = QuadTreePoint(10.0, 10.0, "out")
        self.assertFalse(self.quad_tree.insert(point))

    def test_subdivision(self):
        point1 = QuadTreePoint(1.0, 1.0, "a")
        point2 = QuadTreePoint(2.0, 2.0, "b")
        self.quad_tree.insert(point1)
        self.quad_tree.insert(point2)
        self.assertTrue(self.quad_tree.root.divided)
        self.assertIsNotNone(self.quad_tree.root.nw)
        self.assertIsNotNone(self.quad_tree.root.ne)
        self.assertIsNotNone(self.quad_tree.root.sw)
        self.assertIsNotNone(self.quad_tree.root.se)

    def test_subdivision_capacity(self):
        points = [
            QuadTreePoint(1.0, 1.0, "a"),
            QuadTreePoint(2.0, 2.0, "b"),
            QuadTreePoint(3.0, 3.0, "c"),
            QuadTreePoint(4.0, 4.0, "d"),
            QuadTreePoint(5.0, 5.0, "e"),
        ]
        for point in points:
            self.quad_tree.insert(point)
        self.assertTrue(self.quad_tree.root.divided)

    def test_subdivision_capacity_exceeds(self):
        points = [
            QuadTreePoint(1.0, 1.0, "a"),
            QuadTreePoint(2.0, 2.0, "b"),
            QuadTreePoint(3.0, 3.0, "c"),
            QuadTreePoint(4.0, 4.0, "d"),
            QuadTreePoint(5.0, 5.0, "e"),
            QuadTreePoint(6.0, 6.0, "f"),
        ]
        for point in points:
            self.quad_tree.insert(point)
        self.assertTrue(self.quad_tree.root.divided)

    def test_subdivision_capacity_exceeds(self):
        points = [
            QuadTreePoint(1.0, 1.0, "a"),
            QuadTreePoint(2.0, 2.0, "b"),
            QuadTreePoint(3.0, 3.0, "c"),
            QuadTreePoint(4.0, 4.0, "d"),
            QuadTreePoint(5.0, 5.0, "e"),
            QuadTreePoint(6.0, 6.0, "f"),
        ]
        for point in points:
            self.quad_tree.insert(point)
        self.assertTrue(self.quad_tree.root.divided)

    def test_subdivision_capacity_exceeds(self):
        points = [
            QuadTreePoint(1.0, 1.0, "a"),
            QuadTreePoint(2.0, 2.0, "b"),
            QuadTreePoint(3.0, 3.0, "c"),
            QuadTreePoint(4.0, 4.0, "d"),
            QuadTreePoint(5.0, 5.0, "e"),
            QuadTreePoint(6.0, 6.0, "f"),
        ]
        for point in points:
            self.quad_tree.insert(point)
        self.assertTrue(self.quad_tree.root.divided)

    def test_subdivision_capacity_exceeds(self):
        points = [
            QuadTreePoint(1.0, 1.0, "a"),
            QuadTreePoint(2.0, 2.0, "b"),
            QuadTreePoint(3.0, 3.0, "c"),
            QuadTreePoint(4.0, 4.0, "d"),
            QuadTreePoint(5.0, 5.0, "e"),
            QuadTreePoint(6.0, 6.0, "f"),
        ]
        for point in points:
            self.quad_tree.insert(point)
        self.assertTrue(self.quad_tree.root.divided)

    def test_subdivision_capacity_exceeds(self):
        points = [
            QuadTreePoint(1.0, 1.0, "a"),
            QuadTreePoint(2.0, 2.0, "b"),
            QuadTreePoint(3.0, 3.0, "c"),
            QuadTreePoint(4.0, 4.0, "d"),
            QuadTreePoint(5.0, 5.0, "e"),
            QuadTreePoint(6.0, 6.0, "f"),
        ]
        for point in points:
            self.quad_tree.insert(point)
        self.assertTrue(self.quad_tree.root.divided)

    def test_subdivision_capacity_exceeds(self):
        points = [
            QuadTreePoint(1.0, 1.0, "a"),
            QuadTreePoint(2.0, 2.0, "b"),
            QuadTreePoint(3.0, 3.0, "c"),
            QuadTreePoint(4.0, 4.0, "d"),
            QuadTreePoint(5.0, 5.0, "e"),
            QuadTreePoint(6.0, 6.0, "f"),
        ]
        for point in points:
            self.quad_tree.insert(point)
        self.assertTrue(self.quad_tree.root.divided)

    def test_subdivision_capacity_exceeds(self):
        points = [
            QuadTreePoint(1.0, 1.0, "a"),
            QuadTreePoint(2.0, 2.0, "b"),
            QuadTreePoint(3.0, 3.0, "c"),
            QuadTreePoint(4.0, 4.0, "d"),