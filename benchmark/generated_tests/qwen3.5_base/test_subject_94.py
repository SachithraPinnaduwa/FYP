import unittest

class TestTemporalCache(unittest.TestCase):
    def setUp(self):
        self.cache = TemporalCache()

    def test_put_and_get_latest(self):
        self.cache.put("user1", {"name": "Alice"})
        self.assertEqual(self.cache.get_latest("user1"), {"name": "Alice"})

    def test_put_and_get_latest_multiple_updates(self):
        self.cache.put("user1", {"name": "Alice"})
        self.cache.put("user1", {"name": "Bob"})
        self.assertEqual(self.cache.get_latest("user1"), {"name": "Bob"})

    def test_get_as_of(self):
        self.cache.put("user1", {"name": "Alice"})
        self.cache.put("user1", {"name": "Bob"})
        self.assertEqual(self.cache.get_as_of("user1", time.time()), {"name": "Bob"})
        self.assertEqual(self.cache.get_as_of("user1", time.time() - 1), {"name": "Alice"})

    def test_get_as_of_nonexistent_key(self):
        self.assertEqual(self.cache.get_as_of("nonexistent", time.time()), None)

    def test_get_as_of_before_first_update(self):
        self.cache.put("user1", {"name": "Alice"})
        self.assertEqual(self.cache.get_as_of("user1", 0), None)

if __name__ == '__main__':
    unittest.main()
