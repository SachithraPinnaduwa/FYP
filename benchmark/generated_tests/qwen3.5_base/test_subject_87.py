import unittest

class TestJsonPatch(unittest.TestCase):
    def setUp(self):
        self.patch = JsonPatch({
            "name": "John",
            "age": 30,
            "address": {
                "city": "New York",
                "zip": "10001"
            }
        })

    def test_add_root(self):
        patch = [{"op": "add", "path": "/", "value": "New Value"}]
        result = self.patch.apply(patch)
        self.assertEqual(result, "New Value")

    def test_add_nested(self):
        patch = [{"op": "add", "path": "address/zip", "value": "12345"}]
        result = self.patch.apply(patch)
        self.assertEqual(result["address"]["zip"], "12345")

    def test_replace_nested(self):
        patch = [{"op": "replace", "path": "address/zip", "value": "54321"}]
        result = self.patch.apply(patch)
        self.assertEqual(result["address"]["zip"], "54321")

    def test_remove_nested(self):
        patch = [{"op": "remove", "path": "address/zip"}]
        result = self.patch.apply(patch)
        self.assertNotIn("zip", result["address"])

    def test_multiple_operations(self):
        patch = [
            {"op": "add", "path": "age", "value": 25},
            {"op": "replace", "path": "name", "value": "Jane"},
            {"op": "remove", "path": "address/zip"}
        ]
        result = self.patch.apply(patch)
        self.assertEqual(result["name"], "Jane")
        self.assertEqual(result["age"], 25)
        self.assertNotIn("zip", result["address"])

    def test_invalid_path(self):
        patch = [{"op": "replace", "path": "invalid/path", "value": "value"}]
        with self.assertRaises(ValueError):
            self.patch.apply(patch)

    def test_replace_nonexistent_key(self):
        patch = [{"op": "replace", "path": "name", "value": "Jane"}]
        with self.assertRaises(KeyError):
            self.patch.apply(patch)

if __name__ == "__main__":
    unittest.main()
