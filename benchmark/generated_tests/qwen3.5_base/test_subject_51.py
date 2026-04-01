import unittest

class TestURLBuilder(unittest.TestCase):
    def test_init(self):
        builder = URLBuilder("https://example.com")
        self.assertEqual(builder.base_url, "https://example.com")
        self.assertEqual(builder.paths, [])
        self.assertEqual(builder.query_params, {})

    def test_add_path(self):
        builder = URLBuilder("https://example.com")
        builder.add_path("/path1")
        self.assertEqual(builder.paths, ["path1"])
        self.assertEqual(builder.build(), "https://example.com/path1")

    def test_add_multiple_paths(self):
        builder = URLBuilder("https://example.com")
        builder.add_path("/path1").add_path("/path2")
        self.assertEqual(builder.paths, ["path1", "path2"])
        self.assertEqual(builder.build(), "https://example.com/path1/path2")

    def test_add_query(self):
        builder = URLBuilder("https://example.com")
        builder.add_query("key", "value")
        self.assertEqual(builder.query_params, {"key": "value"})
        self.assertEqual(builder.build(), "https://example.com?key=value")

    def test_add_query_multiple(self):
        builder = URLBuilder("https://example.com")
        builder.add_query("key1", "value1").add_query("key2", "value2")
        self.assertEqual(builder.query_params, {"key1": "value1", "key2": "value2"})
        self.assertEqual(builder.build(), "https://example.com?key1=value1&key2=value2")

    def test_build_with_path_and_query(self):
        builder = URLBuilder("https://example.com")
        builder.add_path("/path1").add_query("key", "value")
        self.assertEqual(builder.build(), "https://example.com/path1?key=value")

    def test_build_with_trailing_slash(self):
        builder = URLBuilder("https://example.com/")
        builder.add_path("/path1")
        self.assertEqual(builder.build(), "https://example.com/path1")

    def test_build_with_empty_paths_and_query(self):
        builder = URLBuilder("https://example.com")
        builder.add_path("").add_query("key", "value")
        self.assertEqual(builder.build(), "https://example.com?key=value")

    def test_build_with_special_characters_in_query(self):
        builder = URLBuilder("https://example.com")
        builder.add_query("key", "value with spaces")
        self.assertEqual(builder.build(), "https://example.com?key=value%20with%20spaces")

    def test_build_with_special_characters_in_path(self):
        builder = URLBuilder("https://example.com")
        builder.add_path("/path/with/special%20chars")
        self.assertEqual(builder.build(), "https://example.com/path/with/special%20chars")

    def test_build_with_multiple_query_params(self):
        builder = URLBuilder("https://example.com")
        builder.add_query("key1", "value1").add_query("key2", "value2")
        self.assertEqual(builder.build(), "https://example.com?key1=value1&key2=value2")

    def test_build_with_empty_query_params(self):
        builder = URLBuilder("https://example.com")
        self.assertEqual(builder.build(), "https://example.com")

    def test_build_with_empty_path(self):
        builder = URLBuilder("https://example.com")
        builder.add_path("")
        self.assertEqual(builder.build(), "https://example.com")

    def test_build_with_multiple_paths_and_query(self):
        builder = URLBuilder("https://example.com")
        builder.add_path("/path1").add_path("/path2").add_query("key", "value")
        self.assertEqual(builder.build(), "https://example.com/path1/path2?key=value")

    def test_build_with_special_characters_in_path_and_query(self):
        builder = URLBuilder("https://example.com")
        builder.add_path("/path/with/special%20chars").add_query("key", "value with spaces")
        self.assertEqual(builder.build(), "https://example.com/path/with/special%20chars?key=value%20with%20spaces")

    def test_build_with_multiple_query_params_and_path(self):
        builder = URLBuilder("https://example.com")
        builder.add_path("/path1").add_query("key1", "value1").add_query("key2", "value2")
        self.assertEqual(builder.build(), "https://example.com/path1?key1=value1&key2=value2")

    def test_build_with_empty_path_and_multiple_query_params(self):
        builder = URLBuilder("https://example.com")
        builder.add_path("").add_query("key1", "value1").add_query("key2", "value2")
        self.assertEqual(builder.build(), "https://example.com?key1=value1&key2=value2")

    def test_build_with_special_characters_in_path_and_multiple_query_params(self):
        builder = URLBuilder("https://example.com")
        builder.add_path("/path/with/special%20chars").add_query("key1", "value1").add_query("key2", "value2")
        self.assertEqual(builder.build(), "https://example.com/path/with/special%20chars?key1=value1&key2=value2")

    def test_build_with_special_characters_in_query_and_path(self):
        builder = URLBuilder("https://example.com")
        builder.add_query("key", "value with spaces").add_path("/path/with/special%20chars")
        self.assertEqual(builder.build(), "https://example.com/path/with/special%20chars?key=value%20with%20spaces")

    def test_build_with_special_characters_in_query_and_multiple_paths(self):
        builder = URLBuilder("https://example.com")
        builder.add_query("key", "value with spaces").add_path("/path1").add_path("/path2")
        self.assertEqual(builder.build(), "https://example.com/path1/path2?key=value%20with%20spaces")

    def test_build_with_special_characters_in_path_and_multiple_query_params(self):
        builder = URLBuilder("https://example.com")
        builder.add_path("/path/with/special%20chars").add_query("key1", "value1").add_query("key2", "value2")
        self.assertEqual(builder.build(), "https://example.com/path/with/special%20chars?key1=value1&key2=value2")

    def test_build_with_special_characters_in_query_and_multiple_paths(self):
        builder = URLBuilder("https://example.com")
        builder.add_query("key", "value with spaces").add_path("/path1").add_path("/path2")
        self.assertEqual(builder.build(), "https://example.com/path1/path2?key=value%20with%20spaces")

    def test_build_with_special_characters_in_path_and_multiple_query_params(self):
        builder = URLBuilder("https://example.com")
        builder.add_path("/path/with/special%20chars").add_query("