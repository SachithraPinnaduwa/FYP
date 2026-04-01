import unittest

class TestTfIdfScorer(unittest.TestCase):
    def setUp(self):
        self.scorer = TfIdfScorer()
        
    def test_add_document(self):
        self.scorer.add_document("doc1", "hello world")
        self.scorer.add_document("doc2", "hello there")
        self.assertEqual(self.scorer.total_docs, 2)
        self.assertEqual(self.scorer.doc_freq.get("hello"), 2)
        self.assertEqual(self.scorer.doc_freq.get("world"), 1)
        self.assertEqual(self.scorer.doc_freq.get("there"), 1)
        
    def test_get_score(self):
        self.scorer.add_document("doc1", "hello world")
        self.scorer.add_document("doc2", "hello there")
        
        score_hello = self.scorer.get_score("hello", "doc1")
        self.assertGreater(score_hello, 0)
        
        score_world = self.scorer.get_score("world", "doc1")
        self.assertGreater(score_world, 0)
        
        score_there = self.scorer.get_score("there", "doc1")
        self.assertEqual(score_there, 0)
        
    def test_case_insensitivity(self):
        self.scorer.add_document("doc1", "Hello World")
        self.scorer.add_document("doc2", "hello world")
        
        score_hello = self.scorer.get_score("hello", "doc1")
        self.assertGreater(score_hello, 0)
        
        score_world = self.scorer.get_score("world", "doc1")
        self.assertGreater(score_world, 0)
        
    def test_empty_document(self):
        self.scorer.add_document("doc1", "")
        self.assertEqual(self.scorer.total_docs, 1)
        self.assertEqual(self.scorer.doc_freq, {})
        
    def test_duplicate_words(self):
        self.scorer.add_document("doc1", "hello hello hello")
        self.assertEqual(self.scorer.documents["doc1"]["hello"], 3)
        
    def test_nonexistent_document(self):
        self.scorer.add_document("doc1", "hello")
        self.assertEqual(self.scorer.get_score("hello", "nonexistent"), 0.0)
        
    def test_nonexistent_word(self):
        self.scorer.add_document("doc1", "hello")
        self.assertEqual(self.scorer.get_score("world", "doc1"), 0.0)
        
    def test_single_document(self):
        self.scorer.add_document("doc1", "hello")
        self.assertEqual(self.scorer.total_docs, 1)
        self.assertEqual(self.scorer.doc_freq.get("hello"), 1)
        
    def test_large_corpus(self):
        words = ["word" + str(i) for i in range(100)]
        for i, word in enumerate(words):
            self.scorer.add_document(f"doc{i}", word)
        self.assertEqual(self.scorer.total_docs, 100)
        self.assertEqual(self.scorer.doc_freq.get("word1"), 1)
        self.assertEqual(self.scorer.doc_freq.get("word100"), 1)
        
    def test_score_consistency(self):
        self.scorer.add_document("doc1", "hello world")
        self.scorer.add_document("doc2", "hello world")
        
        score_hello = self.scorer.get_score("hello", "doc1")
        score_hello_doc2 = self.scorer.get_score("hello", "doc2")
        
        self.assertEqual(score_hello, score_hello_doc2)
        
    def test_score_variation(self):
        self.scorer.add_document("doc1", "hello world")
        self.scorer.add_document("doc2", "hello there")
        
        score_hello_doc1 = self.scorer.get_score("hello", "doc1")
        score_hello_doc2 = self.scorer.get_score("hello", "doc2")
        
        self.assertGreater(score_hello_doc1, score_hello_doc2)
        
    def test_score_with_special_characters(self):
        self.scorer.add_document("doc1", "hello, world!")
        self.scorer.add_document("doc2", "hello world")
        
        score_hello = self.scorer.get_score("hello", "doc1")
        self.assertGreater(score_hello, 0)
        
    def test_score_with_numbers(self):
        self.scorer.add_document("doc1", "hello123 world")
        self.scorer.add_document("doc2", "hello world")
        
        score_hello = self.scorer.get_score("hello", "doc1")
        self.assertGreater(score_hello, 0)
        
    def test_score_with_unicode(self):
        self.scorer.add_document("doc1", "héllo wörld")
        self.scorer.add_document("doc2", "hello world")
        
        score_héllo = self.scorer.get_score("héllo", "doc1")
        self.assertGreater(score_héllo, 0)
        
    def test_score_with_empty_string(self):
        self.scorer.add_document("doc1", "")
        self.scorer.add_document("doc2", "hello")
        
        score_hello = self.scorer.get_score("hello", "doc1")
        self.assertEqual(score_hello, 0.0)
        
    def test_score_with_whitespace(self):
        self.scorer.add_document("doc1", "  hello  world  ")
        self.scorer.add_document("doc2", "hello world")
        
        score_hello = self.scorer.get_score("hello", "doc1")
        self.assertGreater(score_hello, 0)
        
    def test_score_with_tabs(self):
        self.scorer.add_document("doc1", "hello\tworld")
        self.scorer.add_document("doc2", "hello world")
        
        score_hello = self.scorer.get_score("hello", "doc1")
        self.assertGreater(score_hello, 0)
        
    def test_score_with_newlines(self):
        self.scorer.add_document("doc1", "hello\nworld")
        self.scorer.add_document("doc2", "hello world")
        
        score_hello = self.scorer.get_score("hello", "doc1")
        self.assertGreater(score_hello, 0)
        
    def test_score_with_multiple_spaces(self):
        self.scorer.add_document("doc1", "hello  world")
        self.scorer.add_document("doc2", "hello world")
        
        score_hello = self.scorer.get_score("hello", "doc1")
        self.assertGreater(score_hello, 0)
        
    def test_score_with_multiple_newlines(self):
        self.scorer.add_document("doc1", "hello\n\n