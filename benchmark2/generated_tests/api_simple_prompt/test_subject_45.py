from subject_45 import *

import unittest

def format_repeated_string(string, n):
    return '"{}" repeated {} times is: "{}"'.format(string, n, string * n)

class TestFormatRepeatedString(unittest.TestCase):
    def test_repeater_with_single_character(self):
        self.assertEqual(format_repeated_string('a', 3), '"a" repeated 3 times is: "aaa"')
    
    def test_repeater_with_multiple_characters(self):
        self.assertEqual(format_repeated_string('hello', 2), '"hello" repeated 2 times is: "hellohello"')
    
    def test_repeater_with_empty_string(self):
        self.assertEqual(format_repeater_string('', 5), '"" repeated 5 times is: ""')
    
    def test_repeater_with_number_string(self):
        self.assertEqual(format_repeated_string('123', 4), '"123" repeated 4 times is: "123123123123"')
    
    def test_repeater_with_special_characters(self):
        self.assertEqual(format_repeated_string('!@#', 3), '"!@#" repeated 3 times is: "!@#!@#!@#"')
    
    def test_repeater_with_uppercase_letters(self):
        self.assertEqual(format_repeated_string('ABC', 2), '"ABC" repeated 2 times is: "ABCABC"')
    
    def test_repeater_with_lowercase_letters(self):
        self.assertEqual(format_repeated_string('xyz', 4), '"xyz" repeated 4 times is: "xyzxyzxyzxyz"')
    
    def test_repeater_with_mixed_case_letters(self):
        self.assertEqual(format_repeated_string('AbCdEf', 3), '"AbCdEf" repeated 3 times is: "AbCdEfAbCdEfAbCdEf"')
    
    def test_repeater_with_space(self):
        self.assertEqual(format_repeated_string(' ', 5), '" " repeated 5 times is: "     "')
    
    def test_repeater_with_tab(self):
        self.assertEqual(format_repeated_string('\t', 3), '"\t" repeated 3 times is: "\t\t\t"')
    
    def test_repeater_with_newline(self):
        self.assertEqual(format_repeated_string('\n', 2), '"\n" repeated 2 times is: "\n\n"')

if __name__ == '__main__':
    unittest.main()