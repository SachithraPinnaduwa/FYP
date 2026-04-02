import unittest

class TestLongestRepeatingSubstring(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(longest_repeating_substring(""), "")

    def test_single_character(self):
        self.assertEqual(longest_repeating_substring("a"), "")

    def test_two_identical_characters(self):
        self.assertEqual(longest_repeating_substring("aa"), "a")

    def test_two_different_characters(self):
        self.assertEqual(longest_repeating_substring("ab"), "")

    def test_three_identical_characters(self):
        self.assertEqual(longest_repeating_substring("aaa"), "aa")

    def test_three_different_characters(self):
        self.assertEqual(longest_repeating_substring("abc"), "")

    def test_repeating_substring(self):
        self.assertEqual(longest_repeating_substring("abab"), "ab")

    def test_repeating_substring_with_different_lengths(self):
        self.assertEqual(longest_repeating_substring("ababab"), "abab")

    def test_repeating_substring_with_multiple_occurrences(self):
        self.assertEqual(longest_repeating_substring("abababab"), "abab")

    def test_repeating_substring_with_non_repeating_characters(self):
        self.assertEqual(longest_repeating_substring("abcde"), "")

    def test_repeating_substring_with_non_repeating_substrings(self):
        self.assertEqual(longest_repeating_substring("abcdeabc"), "abc")

    def test_repeating_substring_with_non_repeating_substrings_and_different_lengths(self):
        self.assertEqual(longest_repeating_substring("abcdeabcde"), "abcde")

    def test_repeating_substring_with_non_repeating_substrings_and_multiple_occurrences(self):
        self.assertEqual(longest_repeating_substring("abcdeabcdeabcde"), "abcde")

    def test_repeating_substring_with_non_repeating_substrings_and_multiple_occurrences_and_different_lengths(self):
        self.assertEqual(longest_repeating_substring("abcdeabcdeabcdeabcde"), "abcde")

    def test_repeating_substring_with_non_repeating_substrings_and_multiple_occurrences_and_different_lengths_and_non_repeating_characters(self):
        self.assertEqual(longest_repeating_substring("abcdeabcdeabcdeabcdeabcde"), "abcde")

    def test_repeating_substring_with_non_repeating_substrings_and_multiple_occurrences_and_different_lengths_and_non_repeating_substrings(self):
        self.assertEqual(longest_repeating_substring("abcdeabcdeabcdeabcdeabcdeabcde"), "abcde")

    def test_repeating_substring_with_non_repeating_substrings_and_multiple_occurrences_and_different_lengths_and_non_repeating_substrings_and_non_repeating_characters(self):
        self.assertEqual(longest_repeating_substring("abcdeabcdeabcdeabcdeabcdeabcdeabcde"), "abcde")

    def test_repeating_substring_with_non_repeating_substrings_and_multiple_occurrences_and_different_lengths_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings(self):
        self.assertEqual(longest_repeating_substring("abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde"), "abcde")

    def test_repeating_substring_with_non_repeating_substrings_and_multiple_occurrences_and_different_lengths_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters(self):
        self.assertEqual(longest_repeating_substring("abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde"), "abcde")

    def test_repeating_substring_with_non_repeating_substrings_and_multiple_occurrences_and_different_lengths_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings(self):
        self.assertEqual(longest_repeating_substring("abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde"), "abcde")

    def test_repeating_substring_with_non_repeating_substrings_and_multiple_occurrences_and_different_lengths_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters(self):
        self.assertEqual(longest_repeating_substring("abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde"), "abcde")

    def test_repeating_substring_with_non_repeating_substrings_and_multiple_occurrences_and_different_lengths_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings(self):
        self.assertEqual(longest_repeating_substring("abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde"), "abcde")

    def test_repeating_substring_with_non_repeating_substrings_and_multiple_occurrences_and_different_lengths_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters(self):
        self.assertEqual(longest_repeating_substring("abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde"), "abcde")

    def test_repeating_substring_with_non_repeating_substrings_and_multiple_occurrences_and_different_lengths_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings(self):
        self.assertEqual(longest_repeating_substring("abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde"), "abcde")

    def test_repeating_substring_with_non_repeating_substrings_and_multiple_occurrences_and_different_lengths_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters(self):
        self.assertEqual(longest_repeating_substring("abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde"), "abcde")

    def test_repeating_substring_with_non_repeating_substrings_and_multiple_occurrences_and_different_lengths_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings_and_non_repeating_characters_and_non_repeating_substrings(self):
        self.assertEqual(longest_repeating_substring("abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde"), "abcde")

    def test_repeating_substring_with_non