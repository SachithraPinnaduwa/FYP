from subject_79 import *

import unittest

def reverse_string(s):
    chars = list(s)
    length = len(chars)
    for i in range(length // 2):
        chars[i], chars[length - i - 1] = chars[length - i - 1], chars[i]
    return ''.join(chars)

class TestReverseString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")
    
    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")
    
    def test_even_length_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_odd_length_string(self):
        self.assertEqual(reverse_string("world"), "dlrow")
    
    def test_string_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
    
    def test_string_with_special_characters(self):
        self.assertEqual(reverse_string("123!@#"), "#@!321")
    
    def test_string_with_unicode_characters(self):
        self.assertEqual(reverse_string("こんにちは"), "こんにちは")
    
    def test_string_with_mixed_characters(self):
        self.assertEqual(reverse_string("abc123!@#"), "#@!321cba")

if __name__ == '__main__':
    unittest.main()