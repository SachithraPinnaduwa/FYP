from subject_80 import *

import unittest

def check_substring(base_string, sub_string):
    # Convert both strings to lowercase for case-insensitive comparison
    base_string = base_string.lower()
    sub_string = sub_string.lower()
    
    # Check if the sub-string appears in the base string
    return sub_string in base_string

class TestCheckSubstring(unittest.TestCase):
    def test_substring_present(self):
        self.assertTrue(check_substring("Hello World", "world"))
    
    def test_substring_not_present(self):
        self.assertFalse(check_substring("Hello World", "Python"))
    
    def test_case_insensitivity(self):
        self.assertTrue(check_substring("Python Programming", "PYTHON"))
    
    def test_empty_substring(self):
        self.assertTrue(check_substring("Hello World", ""))
    
    def test_empty_base_string(self):
        self.assertFalse(check_substring("", "Python"))
    
    def test_whitespace(self):
        self.assertTrue(check_substring("Hello World", "o w"))
    
    def test_special_characters(self):
        self.assertTrue(check_substring("Hello, World!", "world"))
    
    def test_long_strings(self):
        base = "This is a very long string that should be used to test the substring function."
        sub = "very long"
        self.assertTrue(check_substring(base, sub))

if __name__ == '__main__':
    unittest.main()