import unittest

class TestTTLCache(unittest.TestCase):
    def setUp(self):
        self.cache = TTLCache()

    def test_set_and_get(self):
        self.cache.set("key1", "value1", 10)
        self.assertEqual(self.cache.get("key1"), "value1")

    def test_expired_key(self):
        self.cache.set("key2", "value2", 0)
        self.assertEqual(self.cache.get("key2"), None)

    def test_multiple_keys(self):
        self.cache.set("key3", "value3", 10)
        self.cache.set("key4", "value4", 10)
        self.assertEqual(self.cache.get("key3"), "value3")
        self.assertEqual(self.cache.get("key4"), "value4")

    def test_overwrite_key(self):
        self.cache.set("key1", "value1", 10)
        self.cache.set("key1", "value2", 10)
        self.assertEqual(self.cache.get("key1"), "value2")

    def test_nonexistent_key(self):
        self.assertEqual(self.cache.get("nonexistent"), None)

if __name__ == '__main__':
    unittest.main()
