import unittest

class TestHashTable(unittest.TestCase):
    def test_create_hash_table(self):
        ht = createHashTable(10)
        self.assertEqual(ht.size, 10)
        self.assertEqual(len(ht.__buckets), 10)

    def test_insert(self):
        ht = createHashTable(10)
        ht.insert('key1', 'value1')
        ht.insert('key2', 'value2')
        self.assertEqual(ht.retrieve('key1'), 'value1')
        self.assertEqual(ht.retrieve('key2'), 'value2')

    def test_retrieve(self):
        ht = createHashTable(10)
        ht.insert('key1', 'value1')
        ht.insert('key2', 'value2')
        self.assertEqual(ht.retrieve('key1'), 'value1')
        self.assertEqual(ht.retrieve('key2'), 'value2')
        self.assertIsNone(ht.retrieve('key3'))

    def test_delete(self):
        ht = createHashTable(10)
        ht.insert('key1', 'value1')
        ht.insert('key2', 'value2')
        ht.delete('key1')
        self.assertIsNone(ht.retrieve('key1'))
        self.assertEqual(ht.retrieve('key2'), 'value2')

    def test_collision_resolution(self):
        ht = createHashTable(10)
        ht.insert('key1', 'value1')
        ht.insert('key2', 'value2')
        ht.insert('key10', 'value10')  # Collision with 'key1'
        self.assertEqual(ht.retrieve('key1'), 'value1')
        self.assertEqual(ht.retrieve('key2'), 'value2')
        self.assertEqual(ht.retrieve('key10'), 'value10')

if __name__ == '__main__':
    unittest.main()