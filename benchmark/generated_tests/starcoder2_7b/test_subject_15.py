import unittest

class HashTableTest(unittest.TestCase):
    def setUp(self):
        self.hash_table = createHashTable(10)

    def test_insert(self):
        self.hash_table.insert('key1', 'value1')
        self.assertEqual(self.hash_table.retrieve('key1'), 'value1')

    def test_retrieve(self):
        self.hash_table.insert('key1', 'value1')
        self.assertEqual(self.hash_table.retrieve('key1'), 'value1')

    def test_delete(self):
        self.hash_table.insert('key1', 'value1')
        self.hash_table.delete('key1')
        self.assertEqual(self.hash_table.retrieve('key1'), None)

if __name__ == '__main__':
    unittest.main()