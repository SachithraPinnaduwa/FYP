import unittest

class TestDelete(unittest.TestCase):
    def test_delete(self):
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.left = Node(2)
        root.left.right = Node(7)
        root.right.left = Node(12)
        root.right.right = Node(17)

        root = delete(root, 10)
        self.assertEqual(root.key, 12)
        self.assertEqual(root.left.key, 7)
        self.assertEqual(root.right.key, 17)
        self.assertEqual(root.left.left.key, 5)
        self.assertEqual(root.left.right.key, 15)
        self.assertEqual(root.right.left.key, 12)
        self.assertEqual(root.right.right.key, 17)

        root = delete(root, 12)
        self.assertEqual(root.key, 15)
        self.assertEqual(root.left.key, 7)
        self.assertEqual(root.right.key, 17)
        self.assertEqual(root.left.left.key, 5)
        self.assertEqual(root.left.right.key, 10)
        self.assertEqual(root.right.left.key, 17)
        self.assertEqual(root.right.right.key, 17)

        root = delete(root, 17)
        self.assertEqual(root.key, 15)
        self.assertEqual(root.left.key, 7)
        self.assertEqual(root.right.key, 10)
        self.assertEqual(root.left.left.key, 5)
        self.assertEqual(root.left.right.key, 10)
        self.assertEqual(root.right.left.key, 15)
        self.assertEqual(root.right.right.key, None)

        root = delete(root, 15)
        self.assertEqual(root.key, 10)
        self.assertEqual(root.left.key, 7)
        self.assertEqual(root.right.key, 5)
        self.assertEqual(root.left