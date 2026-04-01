import unittest

class TestBloomFilterHash(unittest.TestCase):
    def setUp(self):
        self.bloom = BloomFilterHash()

    def test_insert_and_contains(self):
        self.bloom.insert("test")
        self.assertTrue(self.bloom.contains("test"))

    def test_insert_and_not_contains(self):
        self.bloom.insert("test")
        self.assertFalse(self.bloom.contains("other"))

    def test_multiple_inserts(self):
        self.bloom.insert("test")
        self.bloom.insert("test2")
        self.assertTrue(self.bloom.contains("test"))
        self.assertTrue(self.bloom.contains("test2"))
        self.assertFalse(self.bloom.contains("other"))

    def test_case_insensitive(self):
        self.bloom.insert("Test")
        self.assertTrue(self.bloom.contains("test"))
        self.assertTrue(self.bloom.contains("TEST"))

    def test_unicode(self):
        self.bloom.insert("café")
        self.assertTrue(self.bloom.contains("café"))
        self.assertFalse(self.bloom.contains("cafe"))

    def test_empty_string(self):
        self.bloom.insert("")
        self.assertTrue(self.bloom.contains(""))
        self.assertFalse(self.bloom.contains(" "))

    def test_large_string(self):
        large_string = "a" * 1000
        self.bloom.insert(large_string)
        self.assertTrue(self.bloom.contains(large_string))
        self.assertFalse(self.bloom.contains("b" * 1000))

    def test_capacity_limit(self):
        self.bloom = BloomFilterHash(10)
        for i in range(10):
            self.bloom.insert(f"item{i}")
        self.assertTrue(self.bloom.contains("item0"))
        self.assertTrue(self.bloom.contains("item9"))
        self.assertFalse(self.bloom.contains("item10"))

if __name__ == '__main__':
    unittest.main()
