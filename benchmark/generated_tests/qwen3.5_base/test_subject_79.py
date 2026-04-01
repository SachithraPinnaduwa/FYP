import unittest

class TestMerkleTree(unittest.TestCase):
    def test_empty_tree(self):
        tree = MerkleTree()
        tree.build([])
        self.assertEqual(tree.get_root_hash(), "")

    def test_single_leaf(self):
        tree = MerkleTree()
        tree.build(["single"])
        self.assertEqual(tree.get_root_hash(), tree._hash("single"))

    def test_two_leaves(self):
        tree = MerkleTree()
        tree.build(["a", "b"])
        self.assertEqual(tree.get_root_hash(), tree._hash(tree._hash("a") + tree._hash("b")))

    def test_three_leaves(self):
        tree = MerkleTree()
        tree.build(["a", "b", "c"])
        self.assertEqual(tree.get_root_hash(), tree._hash(tree._hash(tree._hash("a") + tree._hash("b")) + tree._hash("c")))

    def test_four_leaves(self):
        tree = MerkleTree()
        tree.build(["a", "b", "c", "d"])
        self.assertEqual(tree.get_root_hash(), tree._hash(tree._hash(tree._hash("a") + tree._hash("b")) + tree._hash(tree._hash("c") + tree._hash("d"))))

    def test_five_leaves(self):
        tree = MerkleTree()
        tree.build(["a", "b", "c", "d", "e"])
        self.assertEqual(tree.get_root_hash(), tree._hash(tree._hash(tree._hash("a") + tree._hash("b")) + tree._hash(tree._hash("c") + tree._hash("d")) + tree._hash("e")))

    def test_large_dataset(self):
        data = [f"data_{i}" for i in range(100)]
        tree = MerkleTree()
        tree.build(data)
        self.assertIsNotNone(tree.get_root_hash())

    def test_case_sensitivity(self):
        tree = MerkleTree()
        tree.build(["A", "a"])
        self.assertEqual(tree.get_root_hash(), tree._hash(tree._hash("A") + tree._hash("a")))

    def test_unicode(self):
        tree = MerkleTree()
        tree.build(["日本語", "العربية"])
        self.assertIsNotNone(tree.get_root_hash())

    def test_whitespace(self):
        tree = MerkleTree()
        tree.build(["  ", "\t", "\n"])
        self.assertIsNotNone(tree.get_root_hash())

    def test_special_characters(self):
        tree = MerkleTree()
        tree.build(["!", "@", "#", "$", "%"])
        self.assertIsNotNone(tree.get_root_hash())

    def test_mixed_content(self):
        tree = MerkleTree()
        tree.build(["text", "123", "abc", "xyz"])
        self.assertIsNotNone(tree.get_root_hash())

    def test_empty_strings(self):
        tree = MerkleTree()
        tree.build(["", "", ""])
        self.assertIsNotNone(tree.get_root_hash())

    def test_repeated_data(self):
        tree = MerkleTree()
        tree.build(["a", "a", "a", "a"])
        self.assertIsNotNone(tree.get_root_hash())

    def test_large_hash(self):
        tree = MerkleTree()
        tree.build(["x"] * 1000)
        self.assertIsNotNone(tree.get_root_hash())

    def test_mixed_case(self):
        tree = MerkleTree()
        tree.build(["A", "B", "C", "D"])
        self.assertIsNotNone(tree.get_root_hash())

    def test_mixed_length(self):
        tree = MerkleTree()
        tree.build(["a", "bb", "ccc", "dddd"])
        self.assertIsNotNone(tree.get_root_hash())

    def test_mixed_special_chars(self):
        tree = MerkleTree()
        tree.build(["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}", "|", "\\", ";", "<", "=", ">", "?", "@", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "]", "