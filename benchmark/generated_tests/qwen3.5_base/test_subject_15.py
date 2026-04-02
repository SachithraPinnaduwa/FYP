import unittest

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = createHashTable(10)

    def test_insert_and_retrieve(self):
        self.ht.insert("apple", 1)
        self.ht.insert("banana", 2)
        self.ht.insert("cherry", 3)
        
        self.assertEqual(self.ht.retrieve("apple"), 1)
        self.assertEqual(self.ht.retrieve("banana"), 2)
        self.assertEqual(self.ht.retrieve("cherry"), 3)

    def test_retrieve_nonexistent_key(self):
        self.assertEqual(self.ht.retrieve("grape"), None)

    def test_delete(self):
        self.ht.insert("apple", 1)
        self.ht.insert("banana", 2)
        self.ht.delete("apple")
        
        self.assertEqual(self.ht.retrieve("apple"), None)
        self.assertEqual(self.ht.retrieve("banana"), 2)

    def test_multiple_inserts_same_key(self):
        self.ht.insert("apple", 1)
        self.ht.insert("apple", 2)
        
        self.assertEqual(self.ht.retrieve("apple"), 2)

    def test_hash_collision(self):
        self.ht.insert("apple", 1)
        self.ht.insert("banana", 2)
        
        self.assertEqual(self.ht.retrieve("apple"), 1)
        self.assertEqual(self.ht.retrieve("banana"), 2)

if __name__ == '__main__':
    unittest.main()
