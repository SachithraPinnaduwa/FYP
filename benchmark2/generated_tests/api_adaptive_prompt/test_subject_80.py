from subject_80 import *

import unittest

class TestCheckSubstring(unittest.TestCase):
    def test_substring_present(self):
        self.assertTrue(check_substring("Hello World", "world"))

    def test_substring_not_present(self):
        self.assertFalse(check_substring("Hello World", "Python"))

    def test_case_insensitivity(self):
        self.assertTrue(check_substring("Hello World", "hello"))

    def test_empty_substring(self):
        self.assertTrue(check_substring("Hello World", ""))

    def test_empty_base_string(self):
        self.assertFalse(check_substring("", "world"))

    def test_substring_at_beginning(self):
        self.assertTrue(check_substring("Hello World", "Hello"))

    def test_substring_at_end(self):
        self.assertTrue(check_substring("Hello World", "World"))

    def test_substring_in_middle(self):
        self.assertTrue(check_substring("Hello World", "lo W"))

if __name__ == '__main__':
    unittest.main()