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
    def test_normal_case_1(self):
        self.assertEqual(get_most_frequent_words("The quick brown fox jumps over the lazy dog", ['the', 'over'], 3, 2), [('quick', 1), ('brown', 1)])

    def test_normal_case_2(self):
        self.assertEqual(get_most_frequent_words("Hello hello HeLLo", ['hello'], 5, 1), [('HeLLo', 3)])

    def test_normal_case_3(self):
        self.assertEqual(get_most_frequent_words("Hello, hello! 123", ['hello'], 5, 1), [('Hello', 1)])

    def test_normal_case_4(self):
        self.assertEqual(get_most_frequent_words("The the the", ['the'], 3, 1), [('the', 3)])

    def test_normal_case_5(self):
        self.assertEqual(get_most_frequent_words("Hi there", ['the'], 2, 1), [('Hi', 1)])

    def test_normal_case_6(self):
        self.assertEqual(get_most_frequent_words("", ['the'], 2, 1), [])

    def test_normal_case_7(self):
        self.assertEqual(get_most_frequent_words("   ", ['the'], 2, 1), [])

    def test_normal_case_8(self):
        self.assertEqual(get_most_frequent_words("!!!", ['the'], 2, 1), [])

if __name__ == '__main__':
    unittest.main()