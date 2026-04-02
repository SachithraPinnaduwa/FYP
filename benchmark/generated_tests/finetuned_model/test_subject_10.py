import unittest

def reverse_string(input_str):
    reversed_str = ''
    for i in range(len(input_str) - 1, -1, -1):
        reversed_str += input_str[i]
    return reversed_str

class TestReverseString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")
    
    def test_single_character_string(self):
        self.assertEqual(reverse_string("a"), "a")
    
    def test_multiple_characters_string(self):
        self.assertEqual(reverse_string("abc"), "cba")
    
    def test_string_with_duplicates(self):
        self.assertEqual(reverse_string("aaa"), "aaa")
    
    def test_string_with_mixed_characters(self):
        self.assertEqual(reverse_string("abcde"), "edcba")
    
    def test_string_with_uppercase_letters(self):
        self.assertEqual(reverse_string("AbCdEfG"), "GfEdCbA")
    
    def test_string_with_special_characters(self):
        self.assertEqual(reverse_string("!@#$%^&*()"), ")(*&^%$#@!")
    
    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(reverse_string("  hello world  "), "  dlrow olleh  ")
    
    def test_string_with_only_spaces(self):
        self.assertEqual(reverse_string("   "), "   ")
    
    def test_string_with_non_alphabetic_characters(self):
        self.assertEqual(reverse_string("12345"), "54321")
    
    def test_string_with_punctuation(self):
        self.assertEqual(reverse_string("Hello, World!"), "!dlroW ,olleH")
    
    def test_string_with_accented_characters(self):
        self.assertEqual(reverse_string("áéíóú"), "úóíéá")
    
    def test_string_with_emojis(self):
        self.assertEqual(reverse_string("😊"), "😊")

if __name__ == "__main__":
    unittest.main()