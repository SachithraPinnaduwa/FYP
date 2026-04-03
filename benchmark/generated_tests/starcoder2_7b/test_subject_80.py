```python
import unittest

class TestCheckSubstring(unittest.TestCase):
    def test_check_substring(self):
        self.assertEqual(check_substring("Hello World", "hello"), True)
        self.assertEqual(check_substring("Hello World", "world"), True)
        self.assertEqual(check_substring("Hello World", "world!"), False)
        self.assertEqual(check_substring("Hello World", "WORLD"), True)
        self.assertEqual(check_substring("Hello World", "WORLD!"), False)
        self.assertEqual(check_substring("Hello World", "hello world"), True)
        self.assertEqual(check_substring("Hello World", "hello world!"), False)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "Hello World!"), False)
        self.assertEqual(check_substring("Hello World", ""), True)
        self.assertEqual(check_substring("Hello World", "!"), False)
        self.assertEqual(check_substring("", "Hello World"), False)
        self.assertEqual(check_substring("", "!"), False)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "Hello World"), True)
        self.assertEqual(check_substring("Hello World", "