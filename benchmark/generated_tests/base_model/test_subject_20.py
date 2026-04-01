import unittest

class TestAVLTreeDeletion(unittest.TestCase):

    def setUp(self):
        # Helper method to create a simple AVL tree
        class Node:
            def __init__(self, key):
                self.key = key
                self.left = None
                self.right = None
                self.height = 1

        def insert(node, key):
            if not node:
                return Node(key)
            if key < node.key:
                node.left = insert(node.left, key)
            else:
                node.right = insert(node.right, key)

            node.height = 1 + max(get_height(node.left), get_height(node.right))
            balance = get_balance(node)

            if balance > 1:
                if key < node.left.key:
                    return rotate_right(node)
                else:
                    node.left = rotate_left(node.left)
                    return rotate_right(node)

            if balance < -1:
                if key > node.right.key:
                    return rotate_left(node)
                else:
                    node.right = rotate_right(node.right)
                    return rotate_left(node)

            return node

        def get_height(node):
            if node is None:
                return 0
            return node.height

        def get_balance(node):
            if node is None:
                return 0
            return get_height(node.left) - get_height(node.right)

        def rotate_left(z):
            y = z.right
            T2 = y.left

            y.left = z
            z.right = T2

            z.height = 1 + max(get_height(z.left), get_height(z.right))
            y.height = 1 + max(get_height(y.left), get_height(y.right))

            return y

        def rotate_right(z):
            y = z.left
            T3 = y.right

            y.right = z
            z.left = T3

            z.height = 1 + max(get_height(z.left), get_height(z.right))
            y.height = 1 + max(get_height(y.left), get_height(y.right))

            return y

        def delete(root, key):
            if root is None:
                return root
            elif key < root.key:
                root.left = delete(root.left, key)
            elif key > root.key:
                root.right = delete(root.right, key)
            else:
                if root.left is None:
                    temp = root.right
                    root = None
                    return temp
                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp
                else:
                    temp = _get_min_value_node(root.right)
                    root.key = temp.key
                    root.right = delete(root.right, temp.key)

            if root is None:
                return root

            root.height = 1 + max(get_height(root.left), get_height(root.right))
            balance = get_balance(root)

            if balance > 1:
                if get_balance(root.left) >= 0:
                    return rotate_right(root)
                else:
                    root.left = rotate_left(root.left)
                    return rotate_right(root)
            elif balance < -1:
                if get_balance(root.right) <= 0:
                    return rotate_left(root)
                else:
                    root.right = rotate_right(root.right)
                    return rotate_left(root)

            return root

        def _get_min_value_node(root):
            if root is None or root.left is None:
                return root
            return _get_min_value_node(root.left)

        self.insert = insert
        self.get_height = get_height
        self.get_balance = get_balance
        self.rotate_left = rotate_left
        self.rotate_right = rotate_right
        self.delete = delete

    def test_delete_single_node(self):
        root = self.insert(None, 10)
        root = self.delete(root, 10)
        self.assertIsNone(root)

    def test_delete_leaf_node(self):
        root = self.insert(None, 10)
        root = self.insert(root, 5)
        root = self.insert(root, 15)
        root = self.delete(root, 5)
        self.assertEqual(self.get_height(root), 1)
        self.assertEqual(root.key, 10)

    def test_delete_node_with_one_child(self):
        root = self.insert(None, 10)
        root = self.insert(root, 5)
        root = self.insert(root, 15)
        root = self.delete(root, 15)
        self.assertEqual(self.get_height(root), 1)
        self.assertEqual(root.key, 10)

    def test_delete_node_with_two_children(self):
        root = self.insert(None, 10)
        root = self.insert(root, 5)
        root = self.insert(root, 15)
        root = self.insert(root, 7)
        root = self.delete(root, 10)
        self.assertEqual(self.get_height(root), 2)
        self.assertEqual(root.key, 7)
        self.assertEqual(root.right.key, 15)

    def test_delete_root_node(self):
        root = self.insert(None, 10)
        root = self.insert(root, 5)
        root = self.insert(root, 15)
        root = self.insert(root, 7)
        root = self.delete(root, 10)
        self.assertEqual(self.get_height(root), 2)
        self.assertEqual(root.key, 7)
        self.assertEqual(root.right.key, 15)

    def test_delete_from_empty_tree(self):
        root = None
        root = self.delete(root, 10)
        self.assertIsNone(root)

    def test_delete_duplicate_keys(self):
        root = self.insert(None, 10)
        root = self.insert(root, 10)
        root = self.insert(root, 15)
        root = self.delete(root, 10)
        self.assertEqual(self.get_height(root), 1)
        self.assertEqual(root.key, 15)

if __name__ == '__main__':
    unittest.main()