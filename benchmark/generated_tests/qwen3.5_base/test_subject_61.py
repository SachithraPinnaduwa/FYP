import unittest

class TestDocumentIndexer(unittest.TestCase):
    def setUp(self):
        self.indexer = DocumentIndexer()

    def test_add_document(self):
        self.indexer.add_document(1, "Hello world")
        self.assertEqual(self.indexer.doc_store[1], "Hello world")
        self.assertIn("hello", self.indexer.index)
        self.assertIn("world", self.indexer.index)

    def test_search_single_word(self):
        self.indexer.add_document(1, "Hello world")
        self.indexer.add_document(2, "Hello there")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1, 2])

    def test_search_multiple_words(self):
        self.indexer.add_document(1, "Hello world")
        self.indexer.add_document(2, "Hello there")
        results = self.indexer.search("hello world")
        self.assertEqual(results, [1])

    def test_search_nonexistent_word(self):
        self.indexer.add_document(1, "Hello world")
        results = self.indexer.search("nonexistent")
        self.assertEqual(results, [])

    def test_search_case_insensitive(self):
        self.indexer.add_document(1, "Hello World")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_punctuation(self):
        self.indexer.add_document(1, "Hello, world!")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_empty_phrase(self):
        self.indexer.add_document(1, "Hello world")
        results = self.indexer.search("")
        self.assertEqual(results, [])

    def test_search_with_special_characters(self):
        self.indexer.add_document(1, "Hello!@#world")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_numbers(self):
        self.indexer.add_document(1, "Hello 123 world")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_unicode(self):
        self.indexer.add_document(1, "Hello 世界")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_empty_string(self):
        self.indexer.add_document(1, "")
        results = self.indexer.search("hello")
        self.assertEqual(results, [])

    def test_search_with_whitespace(self):
        self.indexer.add_document(1, "   Hello   world   ")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_multiple_spaces(self):
        self.indexer.add_document(1, "Hello    world")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_tabs(self):
        self.indexer.add_document(1, "Hello\tworld")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_newlines(self):
        self.indexer.add_document(1, "Hello\nworld")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case(self):
        self.indexer.add_document(1, "Hello World")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_punctuation(self):
        self.indexer.add_document(1, "Hello, World!")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_numbers(self):
        self.indexer.add_document(1, "Hello 123 World")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_unicode(self):
        self.indexer.add_document(1, "Hello 世界")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_whitespace(self):
        self.indexer.add_document(1, "   Hello   World   ")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_tabs(self):
        self.indexer.add_document(1, "Hello\tWorld")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_newlines(self):
        self.indexer.add_document(1, "Hello\nWorld")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_special_characters(self):
        self.indexer.add_document(1, "Hello!@#World")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_numbers_and_unicode(self):
        self.indexer.add_document(1, "Hello 123 世界")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_numbers_and_whitespace(self):
        self.indexer.add_document(1, "Hello 123   World")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_numbers_and_tabs(self):
        self.indexer.add_document(1, "Hello 123\tWorld")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_numbers_and_newlines(self):
        self.indexer.add_document(1, "Hello 123\nWorld")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_numbers_and_special_characters(self):
        self.indexer.add_document(1, "Hello 123!@#World")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_numbers_and_unicode(self):
        self.indexer.add_document(1, "Hello 123 世界")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_numbers_and_whitespace(self):
        self.indexer.add_document(1, "Hello 123   World")
        results = self.indexer.search("hello")
        self.assertEqual(results, [1])

    def test_search_with_mixed_case_and_numbers_and_tabs(self):
        self.indexer.add_document(1, "Hello 123