import unittest

class TestIsAnagramFunction(unittest.TestCase):
    # Test case for anagrams
    def test_anagrams(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("triangle", "integral"))
        self.assertTrue(is_anagram("hello", "oellh"))

    # Test case for non-anagrams
    def test_non_anagrams(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("apple", "orange"))
        self.assertFalse(is_anagram("racecar", "carrace"))

    # Test case for strings with spaces
    def test_strings_with_spaces(self):
        self.assertFalse(is_anagram("hello world", "world hello"))
        self.assertFalse(is_anagram("hello world", "world hello!"))
        self.assertFalse(is_anagram("hello world", "world hello world"))

    # Test case for case-insensitivity
    def test_case_insensitivity(self):
        self.assertTrue(is_anagram("Listen", "Silent"))
        self.assertTrue(is_anagram("Triangle", "Integral"))
        self.assertTrue(is_anagram("Hello", "Oellh"))

    # Test case for empty strings
    def test_empty_strings(self):
        self.assertTrue(is_anagram("", ""))
        self.assertFalse(is_anagram("", "hello"))
        self.assertFalse(is_anagram("hello", ""))

    # Test case for strings of different lengths
    def test_different_lengths(self):
        self.assertFalse(is_anagram("hello", "hel"))
        self.assertFalse(is_anagram("hello", "helloo"))
        self.assertFalse(is_anagram("hello", "helloo!"))

if __name__ == '__main__':
    pass