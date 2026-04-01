import unittest
from collections import Counter
import re

def get_most_frequent_words(string, stop_words, min_word_length, num_words):
    string = string.lower()
    string = re.sub(r'[^\w\s]', '', string)
    words = string.split()
    words = [word for word in words if word not in stop_words and len(word) >= min_word_length]
    word_counts = Counter(words)
    most_frequent_words = word_counts.most_common(num_words)
    return most_frequent_words

class TestGetMostFrequentWords(unittest.TestCase):

    def test_empty_string(self):
        result = get_most_frequent_words("", ["the", "and"], 3, 2)
        self.assertEqual(result, [])

    def test_no_valid_words(self):
        result = get_most_frequent_words("hello world", ["hello", "world"], 5, 1)
        self.assertEqual(result, [])

    def test_stop_words_and_min_length(self):
        result = get_most_frequent_words("The quick brown fox jumps over the lazy dog", ["the", "over"], 4, 2)
        self.assertEqual(result, [('quick', 1), ('brown', 1)])

    def test_case_insensitivity(self):
        result = get_most_frequent_words("Hello Hello HeLLo", ["he"], 2, 1)
        self.assertEqual(result, [('hello', 3)])

    def test_punctuation_handling(self):
        result = get_most_frequent_words("Hello! World? This is a test.", ["is", "a"], 3, 2)
        self.assertEqual(result, [('hello', 1), ('world', 1)])

    def test_num_words_limit(self):
        result = get_most_frequent_words("one two three four five six", [], 2, 3)
        self.assertEqual(result, [('three', 1), ('four', 1), ('five', 1)])

if __name__ == '__main__':
    unittest.main()