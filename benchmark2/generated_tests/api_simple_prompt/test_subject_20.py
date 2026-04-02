from subject_20 import *

import unittest

class TestAVLTreeDeletion(unittest.TestCase):
    def test_delete_single_node(self):
        root = Node(10)
        root = delete(root, 10)
        self.assertIsNone(root)

    def test_delete_node_with_one_child(self):
        root = Node(10)
        root.left = Node(5)
        root = delete(root, 5)
        self.assertIsNone(root.left)

    def test_delete_node_with_two_children(self):
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root = delete(root, 10)
        self.assertIsNotNone(root)
        self.assertEqual(root.key, 15)
        self.assertIsNone(root.left)

    def test_delete_node_with_duplicate_keys(self):
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.left = Node(3)
        root.left.right = Node(7)
        root = delete(root, 5)
        self.assertIsNotNone(root)
        self.assertEqual(root.key, 7)
        self.assertIsNone(root.left.left)

    def test_delete_node_with_large_avl_tree(self):
        root = Node(10)
        for i in range(1, 1000):
            root = Node(i)
            root = delete(root, i)
            self.assertIsNone(root)

if __name__ == '__main__':
    unittest.main()