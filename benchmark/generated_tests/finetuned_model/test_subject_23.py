import unittest

class TestEntranceFunction(unittest.TestCase):

    # Test case for strings that are anagrams
    def test_anagrams(self):
        # Test with strings that are anagrams of each other
        self.assertTrue(entrance("listen", "silent"))
        self.assertTrue(entrance("triangle", "integral"))

    # Test case for strings that are not anagrams
    def test_non_anagrams(self):
        # Test with strings that are not anagrams of each other
        self.assertFalse(entrance("hello", "world"))
        self.assertFalse(entrance("python", "java"))

    # Test case for strings with different cases
    def test_different_cases(self):
        # Test with strings that have different cases but are anagrams
        self.assertTrue(entrance("Listen", "Silent"))
        self.assertTrue(entrance("Triangle", "Integral"))

    # Test case for strings with whitespace
    def test_whitespace(self):
        # Test with strings that have whitespace but are anagrams
        self.assertTrue(entrance("listen  ", "silent"))
        self.assertTrue(entrance("   triangle", "integral   "))

    # Test case for empty strings
    def test_empty_strings(self):
        # Test with empty strings
        self.assertTrue(entrance("", ""))
        self.assertFalse(entrance("", "hello"))