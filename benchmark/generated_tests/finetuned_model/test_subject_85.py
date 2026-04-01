import unittest

class TestConvertToCamelCase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(convert_to_camel_case(''), '')

    def test_single_word(self):
        self.assertEqual(convert_to_camel_case('hello'), 'hello')

    def test_multiple_words(self):
        self.assertEqual(convert_to_camel_case('hello world'), 'helloWorld')

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(convert_to_camel_case(' hello world '), 'helloWorld')

    def test_multiple_consecutive_spaces(self):
        self.assertEqual(convert_to_camel_case('hello   world'), 'helloWorld')

    def test_special_characters(self):
        self.assertEqual(convert_to_camel_case('hello,world'), 'hello,world')

    def test_numbers(self):
        self.assertEqual(convert_to_camel_case('hello123world'), 'hello123world')

    def test_mixed_characters(self):
        self.assertEqual(convert_to_camel_case('hello, world 123'), 'hello,World123')

    def test_all_uppercase(self):
        self.assertEqual(convert_to_camel_case('HELLO WORLD'), 'helloWorld')

    def test_all_lowercase(self):
        self.assertEqual(convert_to_camel_case('hello world'), 'helloWorld')

    def test_single_space(self):
        self.assertEqual(convert_to_camel_case(' '), '')

    def test_single_uppercase_letter(self):
        self.assertEqual(convert_to_camel_case('H'), 'H')

    def test_single_lowercase_letter(self):
        self.assertEqual(convert_to_camel_case('h'), 'h')