import unittest

class TestAVLTreeDeletion(unittest.TestCase):

    def test_delete_leaf_node(self):
        # Create a simple AVL tree with 3 nodes
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.height = 1
        root.right.height = 1

        # Delete a leaf node (5)
        root = delete(root, 5)

        # Check the structure of the AVL tree after deletion
        self.assertIsNone(root.left)
        self.assertEqual(root.key, 10)
        self.assertEqual(root.height, 1)
        self.assertEqual(root.right.key, 15)
        self.assertEqual(root.right.height, 1)

    def test_delete_node_with_one_child(self):
        # Create an AVL tree with 4 nodes
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.height = 1
        root.right.height = 2
        root.right.left = Node(12)
        root.right.right = Node(20)
        root.right.left.height = 1
        root.right.right.height = 1

        # Delete a node with one child (15)
        root = delete(root, 15)

        # Check the structure of the AVL tree after deletion
        self.assertEqual(root.key, 10)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.right.key, 20)
        self.assertIsNone(root.right.left)
        self.assertIsNone(root.right.right)

    def test_delete_node_with_two_children(self):
        # Create an AVL tree with 5 nodes
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.height = 2
        root.right.height = 2
        root.left.left = Node(3)
        root.left.right = Node(7)
        root.right.left = Node(12)
        root.right.right = Node(20)
        root.left.left.height = 1
        root.left.right.height = 1
        root.right.left.height = 1
        root.right.right.height = 1

        # Delete a node with two children (10)
        root = delete(root, 10)

        # Check the structure of the AVL tree after deletion
        self.assertEqual(root.key, 12)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.left.key, 7)
        self.assertEqual(root.right.key, 20)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)

    def test_delete_root_node(self):
        # Create an AVL tree with 3 nodes
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.height = 1
        root.right.height = 1

        # Delete the root node (10)
        root = delete(root, 10)

        # Check the structure of the AVL tree after deletion
        self.assertEqual(root.key, 15)
        self.assertEqual(root.height, 1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_delete_duplicate_keys(self):
        # Create an AVL tree with duplicate keys
        root = Node(10)
        root.left = Node(5)
        root.right = Node(10)
        root.left.height = 1
        root.right.height = 1
        root.right.left = Node(10)
        root.right.right = Node(20)
        root.right.left.height = 1
        root.right.right.height = 1

        # Delete a duplicate key (10)
        root = delete(root, 10)

        # Check the structure of the AVL tree after deletion
        self.assertEqual(root.key, 20)
        self.assertEqual(root.height, 1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)