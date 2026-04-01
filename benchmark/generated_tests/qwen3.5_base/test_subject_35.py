import unittest

class TestLFUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LFUCache(2)

    def test_put_get(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.assertEqual(self.cache.get(1), 1)
        self.assertEqual(self.cache.get(2), 2)

    def test_put_get_evict(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.assertEqual(self.cache.get(1), None)
        self.assertEqual(self.cache.get(2), 2)
        self.assertEqual(self.cache.get(3), 3)

    def test_put_get_update(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(1, 1)
        self.assertEqual(self.cache.get(1), 1)
        self.assertEqual(self.cache.get(2), 2)

    def test_put_get_update_evict(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.assertEqual(self.cache.get(1), 1)
        self.assertEqual(self.cache.get(2), None)
        self.assertEqual(self.cache.get(3), 3)

    def test_put_get_update_evict_2(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.assertEqual(self.cache.get(1), 1)
        self.assertEqual(self.cache.get(2), 2)
        self.assertEqual(self.cache.get(3), None)

    def test_put_get_update_evict_3(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.assertEqual(self.cache.get(1), 1)
        self.assertEqual(self.cache.get(2), 2)
        self.assertEqual(self.cache.get(3), 3)

    def test_put_get_update_evict_4(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.assertEqual(self.cache.get(1), 1)
        self.assertEqual(self.cache.get(2), 2)
        self.assertEqual(self.cache.get(3), 3)

    def test_put_get_update_evict_5(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.assertEqual(self.cache.get(1), 1)
        self.assertEqual(self.cache.get(2), 2)
        self.assertEqual(self.cache.get(3), 3)

    def test_put_get_update_evict_6(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.assertEqual(self.cache.get(1), 1)
        self.assertEqual(self.cache.get(2), 2)
        self.assertEqual(self.cache.get(3), 3)

    def test_put_get_update_evict_7(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.assertEqual(self.cache.get(1), 1)
        self.assertEqual(self.cache.get(2), 2)
        self.assertEqual(self.cache.get(3), 3)

    def test_put_get_update_evict_8(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.assertEqual(self.cache.get(1), 1)
        self.assertEqual(self.cache.get(2), 2)
        self.assertEqual(self.cache.get(3), 3)

    def test_put_get_update_evict_9(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self.assertEqual(self.cache.get(1), 1)
        self.assertEqual(self.cache.get(2), 2)
        self.assertEqual(self.cache.get(3), 3)

    def test_put_get_update_evict_10(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.put(3, 3)
        self