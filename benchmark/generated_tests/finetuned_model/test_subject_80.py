import unittest

class TestSubstringFunction(unittest.TestCase):

    def test_substring_present(self):
        # Test case where the sub-string is present in the base string
        self.assertTrue(check_substring("Hello World", "world"))

    def test_substring_not_present(self):
        # Test case where the sub-string is not present in the base string
        self.assertFalse(check_substring("Hello World", "Python"))

    def test_substring_case_insensitive(self):
        # Test case where the sub-string is present in the base string but with different case
        self.assertTrue(check_substring("Hello World", "HELLO"))

    def test_substring_empty(self):
        # Test case where the sub-string is an empty string
        self.assertTrue(check_substring("Hello World", ""))

    def test_base_string_empty(self):
        # Test case where the base string is an empty string
        self.assertFalse(check_substring("", "world"))

    def test_substring_is_base_string(self):
        # Test case where the sub-string is the same as the base string
        self.assertTrue(check_substring("Hello World", "Hello World"))

    def test_substring_at_start(self):
        # Test case where the sub-string is at the start of the base string
        self.assertTrue(check_substring("Hello World", "Hello"))

    def test_substring_at_end(self):
        # Test case where the sub-string is at the end of the base string
        self.assertTrue(check_substring("Hello World", "World"))

    def test_substring_in_middle(self):
        # Test case where the sub-string is in the middle of the base string
        self.assertTrue(check_substring("Hello World", "o W"))