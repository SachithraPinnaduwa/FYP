import unittest

class TestInMemoryTable(unittest.TestCase):
    def setUp(self):
        self.table = InMemoryTable("users", ["name", "age", "email"])

    def test_insert(self):
        record = {"name": "Alice", "age": 30, "email": "alice@example.com"}
        self.assertEqual(self.table.insert(record), 1)
        self.assertEqual(self.table.rows[0]["name"], "Alice")

    def test_select_all(self):
        self.table.insert({"name": "Bob", "age": 25, "email": "bob@example.com"})
        results = self.table.select()
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["name"], "Alice")
        self.assertEqual(results[1]["name"], "Bob")

    def test_select_with_conditions(self):
        self.table.insert({"name": "Charlie", "age": 35, "email": "charlie@example.com"})
        results = self.table.select({"age": 35})
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Charlie")

    def test_delete(self):
        self.table.insert({"name": "David", "age": 40, "email": "david@example.com"})
        deleted_count = self.table.delete({"name": "David"})
        self.assertEqual(deleted_count, 1)
        self.assertEqual(len(self.table.rows), 2)

if __name__ == "__main__":
    unittest.main()
