from subject_10 import *

import unittest

def reverse_string(input_str):
    reversed_str = ''
    for i in range(len(input_str) - 1, -1, -1):
        reversed_str += input_str[i]
    return reversed_str

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string('world'), 'dlrow')
        self.assertEqual(reverse_string('python'), 'nohtyp')
        self.assertEqual(reverse_string(''), '')
        self.assertEqual(reverse_string('a'), 'a')
        self.assertEqual(reverse_string('ab'), 'ba')
        self.assertEqual(reverse_string('abc'), 'cba')
        self.assertEqual(reverse_string('abcde'), 'edcba')
        self.assertEqual(reverse_string('abcdef'), 'fedcba')
        self.assertEqual(reverse_string('abcdefg'), 'gfedcba')
        self.assertEqual(reverse_string('abcdefgh'), 'hgfedcba')
        self.assertEqual(reverse_string('abcdefghi'), 'ihgfedcba')
        self.assertEqual(reverse_string('abcdefghij'), 'jihgfedcba')
        self.assertEqual(reverse_string('abcdefghijk'), 'kjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijkl'), 'lkjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijklm'), 'mlkjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmn'), 'nmlkjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmno'), 'onmlkjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnop'), 'ponmlkjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopq'), 'qponmlkjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqr'), 'rqponmlkjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrs'), 'srqponmlkjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrst'), 'tsrqponmlkjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrstu'), 'utsrqponmlkjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrstuv'), 'vutsrqponmlkjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrstuvw'), 'wvutsrqponmlkjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrstuvwx'), 'xwvutsrqponmlkjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrstuvwxy'), 'yxwvutsrqponmlkjihgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrstuvwxyz'), 'zyxwvutsrqponmlkjihgfedcba')

if __name__ == '__main__':
    unittest.main()