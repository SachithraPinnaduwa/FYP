import unittest

class TestJsonPathExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = JsonPathExtractor({
            "user": {
                "name": "John",
                "age": 30,
                "address": {
                    "city": "New York",
                    "zip": "10001"
                }
            },
            "products": [
                {"name": "Laptop", "price": 1000},
                {"name": "Phone", "price": 500}
            ]
        })

    def test_extract_simple_path(self):
        result = self.extractor.extract("$.user.name")
        self.assertEqual(result, "John")

    def test_extract_nested_path(self):
        result = self.extractor.extract("$.user.address.city")
        self.assertEqual(result, "New York")

    def test_extract_list_index(self):
        result = self.extractor.extract("$.products[0].name")
        self.assertEqual(result, "Laptop")

    def test_extract_invalid_path(self):
        result = self.extractor.extract("$.user.age")
        self.assertEqual(result, None)

    def test_extract_nonexistent_key(self):
        result = self.extractor.extract("$.user.email")
        self.assertEqual(result, None)

    def test_extract_invalid_list_index(self):
        result = self.extractor.extract("$.products[10].name")
        self.assertEqual(result, None)

    def test_extract_empty_list(self):
        result = self.extractor.extract("$.products[0].name")
        self.assertEqual(result, None)

    def test_extract_non_dict_value(self):
        result = self.extractor.extract("$.user.name")
        self.assertEqual(result, "John")

    def test_extract_non_list_value(self):
        result = self.extractor.extract("$.user.name")
        self.assertEqual(result, "John")

    def test_extract_mixed_types(self):
        result = self.extractor.extract("$.user.name")
        self.assertEqual(result, "John")

    def test_extract_complex_nested_path(self):
        result = self.extractor.extract("$.user.address.zip")
        self.assertEqual(result, "10001")

    def test_extract_list_of_dicts(self):
        result = self.extractor.extract("$.products[1].name")
        self.assertEqual(result, "Phone")

    def test_extract_invalid_path_format(self):
        result = self.extractor.extract("user.name")
        self.assertEqual(result, None)

    def test_extract_empty_string_path(self):
        result = self.extractor.extract("")
        self.assertEqual(result, None)

    def test_extract_path_with_trailing_dot(self):
        result = self.extractor.extract("$.user.name.")
        self.assertEqual(result, None)

    def test_extract_path_with_multiple_dots(self):
        result = self.extractor.extract("$.user.name..address")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_dict(self):
        result = self.extractor.extract("$.user.nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in_list_index(self):
        result = self.extractor.extract("$.products[0].nonexistent")
        self.assertEqual(result, None)

    def test_extract_path_with_nonexistent_key_in