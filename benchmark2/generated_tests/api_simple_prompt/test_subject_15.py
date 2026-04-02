from subject_15 import *

import unittest

class TestHashTable(unittest.TestCase):
    def test_create_hash_table(self):
        hash_table = createHashTable(10)
        self.assertIsInstance(hash_table, createHashTable(10).__class__)

    def test_insert_and_retrieve(self):
        hash_table = createHashTable(10)
        hash_table.insert('key1', 'value1')
        self.assertEqual(hash_table.retrieve('key1'), 'value1')

    def test_retrieve_non_existent_key(self):
        hash_table = createHashTable(10)
        self.assertIsNone(hash_table.retrieve('non_existent_key'))

    def test_delete_key(self):
        hash_table = createHashTable(10)
        hash_table.insert('key1', 'value1')
        hash_table.delete('key1')
        self.assertIsNone(hash_table.retrieve('key1'))

    def test_collision_resolution(self):
        hash_table = createHashTable(10)
        hash_table.insert('key1', 'value1')
        hash_table.insert('key2', 'value2')
        self.assertEqual(hash_table.retrieve('key1'), 'value1')
        self.assertEqual(hash_table.retrieve('key2'), 'value2')

    def test_delete_from_non_empty_bucket(self):
        hash_table = createHashTable(10)
        hash_table.insert('key1', 'value1')
        hash_table.insert('key2', 'value2')
        hash_table.delete('key1')
        self.assertIsNone(hash_table.retrieve('key1'))
        self.assertEqual(hash_table.retrieve('key2'), 'value2')

if __name__ == '__main__':
    unittest.main()