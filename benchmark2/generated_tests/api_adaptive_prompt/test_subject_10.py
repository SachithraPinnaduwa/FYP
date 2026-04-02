from subject_10 import *

import unittest

class TestReverseString(unittest.TestCase):
    def test_normal_case_simple_string(self):
        self.assertEqual(reverse_string('abcde'), 'edcba')

    def test_normal_case_repeated_characters(self):
        self.assertEqual(reverse_string('aaaaa'), 'aaaaa')

    def test_normal_case_mixed_characters(self):
        self.assertEqual(reverse_string('abracadabra'), 'arbadacarba')

    def test_edge_case_empty_string(self):
        self.assertEqual(reverse_string(''), '')

    def test_edge_case_single_character(self):
        self.assertEqual(reverse_string('a'), 'a')

    def test_error_handling_non_lowercase_letters(self):
        self.assertEqual(reverse_string('abcde123'), '321edcba')

    def test_error_handling_uppercase_letters(self):
        self.assertEqual(reverse_string('Abcde'), 'edcba')

    def test_error_handling_special_characters(self):
        self.assertEqual(reverse_string('abcde!@#'), '#@!edcba')

if __name__ == '__main__':
    unittest.main()