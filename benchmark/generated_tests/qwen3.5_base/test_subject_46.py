import unittest

class TestIsAnagram(unittest.TestCase):
    """
    Test suite for the is_anagram function.
    """
    
    def test_anagram_true(self):
        """
        Test case for valid anagrams.
        """
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("triangle", "integral"))
        self.assertTrue(is_anagram("a", "a"))
        self.assertTrue(is_anagram("", ""))
    
    def test_anagram_false(self):
        """
        Test case for non-anagrams.
        """
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("listen", "silent"))
        self.assertFalse(is_anagram("triangle", "integral"))
        self.assertFalse(is_anagram("a", "b"))
        self.assertFalse(is_anagram("", "a"))
    
    def test_case_insensitivity(self):
        """
        Test case for case insensitivity.
        """
        self.assertTrue(is_anagram("Listen", "silent"))
        self.assertTrue(is_anagram("TRIANGLE", "integral"))
        self.assertTrue(is_anagram("a", "A"))
    
    def test_empty_strings(self):
        """
        Test case for empty strings.
        """
        self.assertTrue(is_anagram("", ""))
        self.assertFalse(is_anagram("", "a"))
        self.assertFalse(is_anagram("a", ""))
    
    def test_single_character(self):
        """
        Test case for single character strings.
        """
        self.assertTrue(is_anagram("a", "a"))
        self.assertFalse(is_anagram("a", "b"))
    
    def test_multiple_characters(self):
        """
        Test case for multiple character strings.
        """
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertFalse(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("triangle", "integral"))
        self.assertFalse(is_anagram("triangle", "integral"))
    
    def test_special_characters(self):
        """
        Test case for strings with special characters.
        """
        self.assertTrue(is_anagram("a1b2", "1a2b"))
        self.assertFalse(is_anagram("a1b2", "1a2c"))
    
    def test_unicode_characters(self):
        """
        Test case for strings with unicode characters.
        """
        self.assertTrue(is_anagram("café", "fécà"))
        self.assertFalse(is_anagram("café", "fécà"))
    
    def test_whitespace(self):
        """
        Test case for strings with whitespace.
        """
        self.assertTrue(is_anagram("listen ", " silent"))
        self.assertFalse(is_anagram("listen ", " silent"))
    
    def test_mixed_case(self):
        """
        Test case for strings with mixed case.
        """
        self.assertTrue(is_anagram("Listen", "silent"))
        self.assertTrue(is_anagram("TRIANGLE", "integral"))
        self.assertTrue(is_anagram("a", "A"))
    
    def test_long_strings(self):
        """
        Test case for long strings.
        """
        self.assertTrue(is_anagram("listen to the rain", "the rain to listen"))
        self.assertFalse(is_anagram("listen to the rain", "the rain to listen"))
    
    def test_repeated_characters(self):
        """
        Test case for strings with repeated characters.
        """
        self.assertTrue(is_anagram("aabbcc", "bbaacc"))
        self.assertFalse(is_anagram("aabbcc", "bbaacc"))
    
    def test_no_common_characters(self):
        """
        Test case for strings with no common characters.
        """
        self.assertFalse(is_anagram("abc", "def"))
        self.assertFalse(is_anagram("abc", "def"))
    
    def test_case_insensitive_unicode(self):
        """
        Test case for case insensitive unicode characters.
        """
        self.assertTrue(is_anagram("Café", "fécà"))
        self.assertFalse(is_anagram("Café", "fécà"))
    
    def test_whitespace_unicode(self):
        """
        Test case for unicode characters with whitespace.
        """
        self.assertTrue(is_anagram("café ", "fécà "))
        self.assertFalse(is_anagram("café ", "fécà "))
    
    def test_mixed_case_unicode(self):
        """
        Test case for mixed case unicode characters.
        """
        self.assertTrue(is_anagram("Café", "fécà"))
        self.assertTrue(is_anagram("TRIANGLE", "integral"))
        self.assertTrue(is_anagram("a", "A"))
    
    def test_long_unicode_strings(self):
        """
        Test case for long unicode strings.
        """
        self.assertTrue(is_anagram("café à la mode", "à la mode café"))
        self.assertFalse(is_anagram("café à la mode", "à la mode café"))
    
    def test_repeated_unicode_characters(self):
        """
        Test case for unicode strings with repeated characters.
        """
        self.assertTrue(is_anagram("café", "fécà"))
        self.assertFalse(is_anagram("café", "fécà"))
    
    def test_no_common_unicode_characters(self):
        """
        Test case for unicode strings with no common characters.
        """
        self.assertFalse(is_anagram("café", "fécà"))
        self.assertFalse(is_anagram("café", "fécà"))
    
    def test_case_insensitive_whitespace_unicode(self):
        """
        Test case for case insensitive unicode characters with whitespace.
        """
        self.assertTrue(is_anagram("Café ", "fécà "))
        self.assertFalse(is_anagram("Café ", "fécà "))
    
    def test_mixed_case_whitespace_unicode(self):
        """
        Test case for mixed case unicode characters with whitespace.
        """
        self.assertTrue(is_anagram("Café ", "fécà "))
        self.assertTrue(is_anagram("TRIANGLE", "integral"))
        self.assertTrue(is_anagram("a", "A"))
    
    def test_long_whitespace_unicode_strings(self):
        """
        Test case for long unicode strings with whitespace.
        """
        self.assertTrue(is_anagram("café à la mode ", "à la mode café "))
        self.assertFalse(is_anagram("café à la mode ", "à la mode café "))
    
    def test_repeated_whitespace_unicode_characters(self):
        """
        Test case for unicode strings with repeated characters and whitespace.
        """
        self.assertTrue(is_anagram("café ", "fécà "))
        self.assertFalse(is_anagram("café ", "fécà "))
    
    def test_no_common_whitespace_unicode_characters(self):
        """
        Test case for unicode strings with no common characters and whitespace.
        """
        self.assertFalse(is_anagram("café ", "fécà "))