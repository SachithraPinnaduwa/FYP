from subject_15 import *

import unittest

class TestHashTable(unittest.TestCase):
    def test_insert_and_retrieve_single_key_value_pair(self):
        size = 10
        key = 'test_key'
        value = 'test_value'
        hash_table = createHashTable(size)
        hash_table.insert(key, value)
        self.assertEqual(hash_table.retrieve(key), value)

    def test_insert_and_retrieve_multiple_key_value_pairs(self):
        size = 10
        key1 = 'key1'
        value1 = 'value1'
        key2 = 'key2'
        value2 = 'value2'
        hash_table = createHashTable(size)
        hash_table.insert(key1, value1)
        hash_table.insert(key2, value2)
        self.assertEqual(hash_table.retrieve(key1), value1)
        self.assertEqual(hash_table.retrieve(key2), value2)

    def test_delete_key_value_pair(self):
        size = 10
        key = 'key_to_delete'
        value = 'value_to_delete'
        hash_table = createHashTable(size)
        hash_table.insert(key, value)
        hash_table.delete(key)
        self.assertIsNone(hash_table.retrieve(key))

    def test_retrieve_non_existent_key(self):
        size = 10
        non_existent_key = 'non_existent_key'
        hash_table = createHashTable(size)
        self.assertIsNone(hash_table.retrieve(non_existent_key))

    def test_non_integer_size_input(self):
        size = 'not_an_integer'
        with self.assertRaises(TypeError):
            createHashTable(size)

    def test_negative_size_input(self):
        size = -10
        with self.assertRaises(ValueError):
            createHashTable(size)

if __name__ == '__main__':
    unittest.main()