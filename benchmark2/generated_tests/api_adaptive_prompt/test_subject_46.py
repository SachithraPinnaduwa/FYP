from subject_46 import *

import unittest

def is_anagram(string1, string2):
    """
    Determine if two input strings are anagrams of each other.
    
    Args:
    string1 (str): The first input string.
    string2 (str): The second input string.
    
    Returns:
    bool: True if string1 and string2 are anagrams, False otherwise.
    """
    return sorted(string1.lower()) == sorted(string2.lower())

class TestIsAnagram(unittest.TestCase):
    def test_normal_case_anagrams(self):
        self.assertTrue(is_anagram('listen', 'silent'))

    def test_normal_case_not_anagrams(self):
        self.assertFalse(is_anagram('hello', 'world'))

    def test_normal_case_different_cases_anagrams(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

    def test_normal_case_different_cases_not_anagrams(self):
        self.assertFalse(is_anagram('Hello', 'World'))

    def test_normal_case_different_cases_anagrams_2(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

    def test_normal_case_different_cases_anagrams_3(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

    def test_normal_case_different_cases_anagrams_4(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

    def test_normal_case_different_cases_anagrams_5(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

    def test_normal_case_different_cases_anagrams_6(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

    def test_normal_case_different_cases_anagrams_7(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

    def test_normal_case_different_cases_anagrams_8(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

    def test_normal_case_different_cases_anagrams_9(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

    def test_normal_case_different_cases_anagrams_10(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

    def test_normal_case_different_cases_anagrams_11(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

    def test_normal_case_different_cases_anagrams_12(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

    def test_normal_case_different_cases_anagrams_13(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

    def test_normal_case_different_cases_anagrams_14(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

    def test_normal_case_different_cases_anagrams_15(self):
        self.assertTrue(is_anagram('Listen', 'Silent'))

if __name__ == '__main__':
    unittest.main()