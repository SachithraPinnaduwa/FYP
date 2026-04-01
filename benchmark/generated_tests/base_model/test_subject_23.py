import unittest

class TestIsAnagram(unittest.TestCase):

    def test_empty_strings(self):
        self.assertTrue(entrance("", ""))

    def test_single_character_anagrams(self):
        self.assertTrue(entrance("a", "a"))
        self.assertFalse(entrance("a", "b"))

    def test_multiple_characters_anagrams(self):
        self.assertTrue(entrance("listen", "silent"))
        self.assertFalse(entrance("hello", "world"))

    def test_different_cases_anagrams(self):
        self.assertTrue(entrance("Listen", "Silent"))
        self.assertFalse(entrance("Hello", "World"))

    def test_whitespace_and_case_anagrams(self):
        self.assertTrue(entrance("dormitory", "dirty room   "))
        self.assertFalse(entrance("School master", "The classroom"))

    def test_same_length_non_anagrams(self):
        self.assertFalse(entrance("apple", "papel"))
        self.assertFalse(entrance("rat", "car"))

if __name__ == '__main__':
    unittest.main()