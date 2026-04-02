from subject_28 import *

import unittest

class TestLongestRepeatingSubstring(unittest.TestCase):
    def test_normal_case_multiple_repeating_substrings(self):
        self.assertEqual(longest_repeating_substring('abcabcabc'), 'abc')

    def test_normal_case_single_repeating_substring(self):
        self.assertEqual(longest_repeating_substring('abcabc'), 'abc')

    def test_normal_case_no_repeating_substrings(self):
        self.assertEqual(longest_repeating_substring('abcdef'), '')

    def test_normal_case_single_character_repeated_multiple_times(self):
        self.assertEqual(longest_repeating_substring('aaaa'), 'a')

    def test_normal_case_multiple_repeating_substrings_of_different_lengths(self):
        self.assertEqual(longest_repeating_substring('abababab'), 'abab')

    def test_normal_case_single_character_repeated_once(self):
        self.assertEqual(longest_repeating_substring('a'), '')

    def test_normal_case_single_character_repeated_multiple_times_with_additional_character(self):
        self.assertEqual(longest_repeating_substring('aaaaa'), 'a')

    def test_normal_case_multiple_repeating_substrings_of_different_lengths_with_additional_character(self):
        self.assertEqual(longest_repeating_substring('ababababa'), 'abab')

    def test_normal_case_single_character_repeated_once_with_additional_character(self):
        self.assertEqual(longest_repeating_substring('aa'), 'a')

if __name__ == '__main__':
    unittest.main()