import unittest

class TestHashTable(unittest.TestCase):

    def test_insert_and_retrieve(self):
        # Test inserting and retrieving a key-value pair
        ht = createHashTable(10)
        ht.insert('key1', 'value1')
        self.assertEqual(ht.retrieve('key1'), 'value1')

    def test_retrieve_nonexistent_key(self):
        # Test retrieving a key that does not exist
        ht = createHashTable(10)
        self.assertIsNone(ht.retrieve('nonexistent_key'))

    def test_delete_key(self):
        # Test deleting a key-value pair
        ht = createHashTable(10)
        ht.insert('key1', 'value1')
        ht.delete('key1')
        self.assertIsNone(ht.retrieve('key1'))

    def test_collision_resolution(self):
        # Test collision resolution using separate chaining
        ht = createHashTable(2)
        ht.insert('key1', 'value1')
        ht.insert('key3', 'value3')  # Collision with 'key1'
        self.assertEqual(ht.retrieve('key1'), 'value1')
        self.assertEqual(ht.retrieve('key3'), 'value3')

    def test_insert_and_delete_multiple(self):
        # Test inserting and deleting multiple key-value pairs
        ht = createHashTable(10)
        ht.insert('key1', 'value1')
        ht.insert('key2', 'value2')
        ht.insert('key3', 'value3')
        ht.delete('key2')
        self.assertEqual(ht.retrieve('key1'), 'value1')
        self.assertIsNone(ht.retrieve('key2'))
        self.assertEqual(ht.retrieve('key3'), 'value3')

    def test_empty_hash_table(self):
        # Test operations on an empty hash table
        ht = createHashTable(10)
        self.assertIsNone(ht.retrieve('key1'))
        ht.insert('key1', 'value1')
        ht.delete('key1')
        self.assertIsNone(ht.retrieve('key1'))