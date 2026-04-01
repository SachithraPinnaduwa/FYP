import unittest

class TestLongestRepeatingSubstring(unittest.TestCase):
    # Test case for a string with a repeating substring
    def test_repeating_substring(self):
        self.assertEqual(longest_repeating_substring("ababab"), "abab")

    # Test case for a string with no repeating substring
    def test_no_repeating_substring(self):
        self.assertEqual(longest_repeating_substring("abcdef"), "")

    # Test case for a string with multiple repeating substrings of the same length
    def test_multiple_repeating_substrings(self):
        self.assertEqual(longest_repeating_substring("abcabcabc"), "abcabc")

    # Test case for a string with a repeating substring at the beginning
    def test_repeating_substring_at_beginning(self):
        self.assertEqual(longest_repeating_substring("abcabcabc"), "abcabc")

    # Test case for a string with a repeating substring at the end
    def test_repeating_substring_at_end(self):
        self.assertEqual(longest_repeating_substring("abcabcabc"), "abcabc")

    # Test case for a string with a repeating substring in the middle
    def test_repeating_substring_in_middle(self):
        self.assertEqual(longest_repeating_substring("abcabcabc"), "abcabc")

    # Test case for an empty string
    def test_empty_string(self):
        self.assertEqual(longest_repeating_substring(""), "")