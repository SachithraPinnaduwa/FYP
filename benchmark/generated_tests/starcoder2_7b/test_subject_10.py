```python
import unittest

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string('abc'), 'cba')
        self.assertEqual(reverse_string('a'), 'a')
        self.assertEqual(reverse_string(''), '')
        self.assertEqual(reverse_string('abcde'), 'edcba')
        self.assertEqual(reverse_string('abcdeabcde'), 'edcbaedcba')
        self.assertEqual(reverse_string('abcdeabcdeabcde'), 'edcbaedcbaedcba')
        self.assertEqual(reverse_string('abcdeabcdeabcdeabcde'), 'edcbaedcbaedcbaedcba')
        self.assertEqual(reverse_string('abcdeabcdeabcdeabcdeabcde'), 'edcbaedcbaedcbaedcbaedcba')
        self.assertEqual(reverse_string('abcdeabcdeabcdeabcdeabcdeabcde'), 'edcbaedcbaedcbaedcbaedcbaedcba')
        self.assertEqual(reverse_string('abcdeabcdeabcdeabcdeabcdeabcdeabcde'), 'edcbaedcbaedcbaedcbaedcbaedcbaedcba')
        self.assertEqual(reverse_string('abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde'), 'edcbaedcbaedcbaedcbaedcbaedcbaedcbaedcba')
        self.assertEqual(reverse_string('abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde'), 'edcbaedcbaedcbaedcbaedcbaedcbaedcbaedcbaedcba')
        self.assertEqual(reverse_string('abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde'), 'edcbaedcbaedcbaedcbaedcbaedcbaedcbaedcbaedcbaedcba')
        self.assertEqual(reverse_string('abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde'), 'edcbaedcbaedcbaedcbaedcbaedcbaedcbaedcbaedcbaedcbaedcba')
        self.assertEqual(reverse_string('abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde'), 'edcbaedcbaedcbaedcbaedcbaedcbaedcbaed