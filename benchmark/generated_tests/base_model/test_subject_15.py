import unittest

class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.table_size = 10
        self.hash_table = createHashTable(self.table_size)

    def test_insert_retrieve(self):
        self.hash_table.insert('apple', 1)
        self.assertEqual(self.hash_table.retrieve('apple'), 1)
        
        self.hash_table.insert('banana', 2)
        self.assertEqual(self.hash_table.retrieve('banana'), 2)
        
        self.hash_table.insert('cherry', 3)
        self.assertEqual(self.hash_table.retrieve('cherry'), 3)

    def test_collision_resolution(self):
        # Insert keys that collide using modulo operation
        self.hash_table.insert('a', 10)
        self.hash_table.insert('b', 20)
        
        # Check if both values can be retrieved
        self.assertEqual(self.hash_table.retrieve('a'), 10)
        self.assertEqual(self.hash_table.retrieve('b'), 20)

    def test_delete(self):
        self.hash_table.insert('date', 4)
        self.hash_table.delete('date')
        self.assertIsNone(self.hash_table.retrieve('date'))

    def test_non_existent_key_retrieve(self):
        result = self.hash_table.retrieve('grape')
        self.assertIsNone(result)

    def test_delete_non_existent_key(self):
        self.hash_table.delete('fig')

if __name__ == '__main__':
    unittest.main()