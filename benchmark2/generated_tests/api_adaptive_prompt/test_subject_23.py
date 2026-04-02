from subject_23 import *

import unittest

def entrance(str1, str2):
    # Convert the input strings to lowercase and remove whitespace
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    # Sort the characters in both strings alphabetically
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare the sorted strings
    return sorted_str1 == sorted_str2

class TestEntranceFunction(unittest.TestCase):
    def test_normal_case_anagrams(self):
        self.assertTrue(entrance('listen', 'silent'))

    def test_normal_case_not_anagrams(self):
        self.assertFalse(entrance('hello', 'world'))

    def test_normal_case_anagrams_with_spaces(self):
        self.assertTrue(entrance('listen ', 'silent'))

    def test_normal_case_not_anagrams_with_spaces(self):
        self.assertFalse(entrance('hello', ' world'))

    def test_edge_case_empty_strings(self):
        self.assertTrue(entrance('', ''))

    def test_edge_case_anagrams_different_cases(self):
        self.assertTrue(entrance('Listen', 'silent'))

    def test_edge_case_not_anagrams_different_cases(self):
        self.assertFalse(entrance('Hello', 'world'))

    def test_error_handling_non_string_inputs(self):
        with self.assertRaises(TypeError):
            entrance(123, 'world')

if __name__ == '__main__':
    unittest.main()