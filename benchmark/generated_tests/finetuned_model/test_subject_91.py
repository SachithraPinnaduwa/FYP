import unittest

def reverse_string(s):
    # Convert the string to a list since strings are immutable
    s = list(s)
    start = 0
    end = len(s) - 1
    
    # Iterate until start is less than end
    while start < end:
        # Swap characters at start and end
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    
    # Convert the list back to a string
    return ''.join(s)

class TestReverseString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")
    
    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")
    
    def test_even_length_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_odd_length_string(self):
        self.assertEqual(reverse_string("world"), "dlrow")
    
    def test_string_with_special_characters(self):
        self.assertEqual(reverse_string("!@#$%^&*()"), ")(&*^%$#@!")
    
    def test_string_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
    
    def test_string_with_numbers(self):
        self.assertEqual(reverse_string("1234567890"), "0987654321")
    
    def test_string_with_mixed_characters(self):
        self.assertEqual(reverse_string("Python3.8"), "8.3nohtyP")
    
    def test_string_with_repeating_characters(self):
        self.assertEqual(reverse_string("aaaaa"), "aaaaa")
    
    def test_string_with_mixed_case(self):
        self.assertEqual(reverse_string("HelloWorld"), "dlroWolleH")

if __name__ == '__main__':
    unittest.main()