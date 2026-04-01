import unittest

class TestIsAnagram(unittest.TestCase):

    def test_is_anagram_true(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("Triangle", "Integral"))
        self.assertTrue(is_anagram("Dormitory", "Dirty room"))

    def test_is_anagram_false(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("Python", "Java"))
        self.assertFalse(is_anagram("OpenAI", "GPT-4"))

    def test_empty_strings(self):
        self.assertTrue(is_anagram("", ""))
        self.assertFalse(is_anagram("", "non-empty"))

    def test_single_character(self):
        self.assertTrue(is_anagram("a", "a"))
        self.assertFalse(is_anagram("a", "b"))

    def test_case_insensitivity(self):
        self.assertTrue(is_anagram("Hello", "oLleh"))
        self.assertFalse(is_anagram("Hello", "World"))

if __name__ == '__main__':
    unittest.main()