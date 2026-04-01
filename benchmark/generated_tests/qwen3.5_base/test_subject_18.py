import unittest

class TestPrefixTree(unittest.TestCase):
    def setUp(self):
        self.prefix_tree = PrefixTree()

    def test_insert_and_search(self):
        self.prefix_tree.insert("apple")
        self.assertTrue(self.prefix_tree.search("apple"))
        self.assertFalse(self.prefix_tree.search("app"))
        self.assertFalse(self.prefix_tree.search("apricot"))

    def test_starts_with(self):
        self.prefix_tree.insert("apple")
        self.assertTrue(self.prefix_tree.starts_with("app"))
        self.assertFalse(self.prefix_tree.starts_with("apricot"))

    def test_multiple_inserts(self):
        self.prefix_tree.insert("cat")
        self.prefix_tree.insert("car")
        self.assertTrue(self.prefix_tree.search("cat"))
        self.assertTrue(self.prefix_tree.search("car"))
        self.assertFalse(self.prefix_tree.search("cub"))

    def test_empty_string(self):
        self.assertTrue(self.prefix_tree.search(""))
        self.assertTrue(self.prefix_tree.starts_with(""))

    def test_special_characters(self):
        self.prefix_tree.insert("hello-world")
        self.assertTrue(self.prefix_tree.search("hello-world"))
        self.assertTrue(self.prefix_tree.starts_with("hello"))

if __name__ == '__main__':
    unittest.main()
