import unittest

class TestGetMostFrequentWords(unittest.TestCase):

    def test_normal_case(self):
        # Test case with normal input
        string = "This is a test string. This string contains some words that appear more than once, and some that appear only once."
        stop_words = ["is", "a", "this"]
        min_word_length = 4
        num_words = 2
        expected_result = [('string', 2), ('contains', 1)]
        self.assertEqual(get_most_frequent_words(string, stop_words, min_word_length, num_words), expected_result)

    def test_no_stop_words(self):
        # Test case with no stop words
        string = "Hello, how are you? Hope you are doing well."
        stop_words = []
        min_word_length = 4
        num_words = 2
        expected_result = [('hello', 1), ('how', 1)]
        self.assertEqual(get_most_frequent_words(string, stop_words, min_word_length, num_words), expected_result)

    def test_no_words_longer_than_min_length(self):
        # Test case with no words longer than the minimum length
        string = "I am a short string."
        stop_words = []
        min_word_length = 6
        num_words = 1
        expected_result = []
        self.assertEqual(get_most_frequent_words(string, stop_words, min_word_length, num_words), expected_result)

    def test_empty_string(self):
        # Test case with an empty string
        string = ""
        stop_words = []
        min_word_length = 1
        num_words = 1
        expected_result = []
        self.assertEqual(get_most_frequent_words(string, stop_words, min_word_length, num_words), expected_result)

    def test_case_insensitivity(self):
        # Test case with case-insensitivity
        string = "Test test TEST"
        stop_words = []
        min_word_length = 4
        num_words = 1
        expected_result = [('test', 3)]
        self.assertEqual(get_most_frequent_words(string, stop_words, min_word_length, num_words), expected_result)

    def test_punctuation_marks(self):
        # Test case with punctuation marks
        string = "Hello, how are you? Hope you are doing well."
        stop_words = []
        min_word_length = 4
        num_words = 2
        expected_result = [('hello', 1), ('how', 1)]
        self.assertEqual(get_most_frequent_words(string, stop_words, min_word_length, num_words), expected_result)

    def test_large_input(self):
        # Test case with a large input
        string = "This is a large test string. This string contains some words that appear more than once, and some that appear only once. This is a test string to check the performance of the function."
        stop_words = ["is", "a", "this"]
        min_word_length = 4
        num_words = 5
        expected_result = [('string', 3), ('contains', 1), ('more', 1), ('than', 1), ('once', 1)]
        self.assertEqual(get_most_frequent_words(string, stop_words, min_word_length, num_words), expected_result)