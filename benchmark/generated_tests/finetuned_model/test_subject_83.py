import unittest
from collections import deque

class TestMakeStringsEqual(unittest.TestCase):

    def test_impossible_case(self):
        # Test the case when it's impossible to make the strings equal
        s = "a"
        t = "b"
        expected_output = -1, []
        self.assertEqual(make_strings_equal(s, t), expected_output)

    def test_equal_strings(self):
        # Test the case when the strings are already equal
        s = "abab"
        t = "abab"
        expected_output = 0, []
        self.assertEqual(make_strings_equal(s, t), expected_output)

    def test_sample_input_1(self):
        # Test the first sample input from the problem statement
        s = "abab"
        t = "aabb"
        expected_output = 2, [(3, 3), (3, 2)]
        self.assertEqual(make_strings_equal(s, t), expected_output)

    def test_sample_input_2(self):
        # Test the second sample input from the problem statement
        s = "babbaabb"
        t = "abababaa"
        expected_output = 3, [(2, 6), (1, 3), (7, 8)]
        self.assertEqual(make_strings_equal(s, t), expected_output)

    def test_large_input(self):
        # Test a large input to ensure the function can handle it
        n = 200000
        s = "a" * n
        t = "b" * n
        expected_output = -1, []
        self.assertEqual(make_strings_equal(s, t), expected_output)

    def test_string_with_single_character(self):
        # Test a string with only a single character
        s = "a"
        t = "a"
        expected_output = 0, []
        self.assertEqual(make_strings_equal(s, t), expected_output)

    def test_string_with_all_a_characters(self):
        # Test a string with all 'a' characters
        s = "aaaa"
        t = "aaaa"
        expected_output = 0, []
        self.assertEqual(make_strings_equal(s, t), expected_output)

    def test_string_with_all_b_characters(self):
        # Test a string with all 'b' characters
        s = "bbbb"
        t = "bbbb"
        expected_output = 0, []
        self.assertEqual(make_strings_equal(s, t), expected_output)