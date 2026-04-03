```python
import unittest

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string('world'), 'dlrow')
        self.assertEqual(reverse_string(''), '')
        self.assertEqual(reverse_string('a'), 'a')
        self.assertEqual(reverse_string('ab'), 'ba')
        self.assertEqual(reverse_string('abc'), 'cba')
        self.assertEqual(reverse_string('abcd'), 'dcba')
        self.assertEqual(reverse_string('abcde'), 'edcba')
        self.assertEqual(reverse_string('abcdef'), 'fedcba')
        self.assertEqual(reverse_string('abcdefgh'), 'hgfedcba')
        self.assertEqual(reverse_string('abcdefghi'), 'ihgfedcba')
        self.assertEqual(reverse_string('abcdefghij'), 'jihgfedcba')
        self.assertEqual(reverse_string('abcdefghijkl'), 'lkjhgfedcba')
        self.assertEqual(reverse_string('abcdefghijklm'),'mlkjhgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmn'), 'nmlkjhgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmno'), 'onmlkjhgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnop'), 'popmlkjhgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopq'), 'qpopmlkjhgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrst'), 'tsrqpopmlkjhgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrstu'), 'utsrqpopmlkjhgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrstuv'), 'vutsrqpopmlkjhgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrstuvw'), 'wvuutsrqpopmlkjhgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrstuvwx'), 'xwvutsrqpopmlkjhgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrstuvwxy'), 'yxwvutsrqpopmlkjhgfedcba')
        self.assertEqual(reverse_string('abcdefghijklmnopqrstuvwxyz'), 'zy