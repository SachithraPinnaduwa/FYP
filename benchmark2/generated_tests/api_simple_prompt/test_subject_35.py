from subject_35 import *

import unittest
import re
from collections import Counter

def get_most_frequent_words(string, stop_words, min_word_length, num_words):
    string = string.lower()
    string = re.sub(r'[^\w\s]', '', string)
    words = string.split()
    words = [word for word in words if word not in stop_words and len(word) >= min_word_length]
    word_counts = Counter(words)
    most_frequent_words = word_counts.most_common(num_words)
    return most_frequent_words

class TestGetMostFrequentWords(unittest.TestCase):
    def test_get_most_frequent_words(self):
        self.assertEqual(get_most_frequent_words("Hello world, hello Python!", ["hello"], 5, 1), [('world,', 1)])
        self.assertEqual(get_most_frequent_words("The quick brown fox jumps over the lazy dog", [], 3, 3), [('the', 2), ('quick', 1), ('brown', 1)])
        self.assertEqual(get_most_frequent_words("A stitch in time saves nine", ["in"], 4, 2), [('time', 1), ('saves', 1)])
        self.assertEqual(get_most_frequent_words("To be or not to be, that is the question", ["be", "or"], 4, 2), [('not', 1), ('that', 1)])
        self.assertEqual(get_most_frequent_words("Lorem ipsum dolor sit amet, consectetur adipiscing elit", ["elit"], 4, 3), [('lorem', 1), ('ipsum', 1), ('dolor', 1)])

if __name__ == '__main__':
    unittest.main()