from subject_85 import *

import unittest

def convert_to_camel_case(string):
    string = string.strip()
    result = ''
    capitalize_next = False

    for char in string:
        if char == ' ':
            capitalize_next = True
        elif capitalize_next:
            result += char.upper()
            capitalize_next = False
        else:
            result += char

    return result

class TestConvertToCamelCase(unittest.TestCase):
    def test_convert_to_camel_case(self):
        self.assertEqual(convert_to_camel_case(''), '')
        self.assertEqual(convert_to_camel_case('hello'), 'hello')
        self.assertEqual(convert_to_camel_case('hello world'), 'helloWorld')
        self.assertEqual(convert_to_camel_case(' hello world '), 'helloWorld')
        self.assertEqual(convert_to_camel_case('hello  world'), 'helloWorld')
        self.assertEqual(convert_to_camel_case('hello_world'), 'helloWorld')
        self.assertEqual(convert_to_camel_case('hello_world '), 'helloWorld')
        self.assertEqual(convert_to_camel_case('hello world '), 'helloWorld')
        self.assertEqual(convert_to_camel_case('hello world!'), 'helloWorld!')
        self.assertEqual(convert_to_camel_case('hello world 123'), 'helloWorld123')
        self.assertEqual(convert_to_camel_case('hello world 123 '), 'helloWorld123')
        self.assertEqual(convert_to_camel_case(' hello world 123 '), 'helloWorld123')
        self.assertEqual(convert_to_camel_case('hello   world'), 'helloWorld')
        self.assertEqual(convert_to_camel_case('hello   world '), 'helloWorld')
        self.assertEqual(convert_to_camel_case(' hello   world '), 'helloWorld')
        self.assertEqual(convert_to_camel_case('hello   world!'), 'helloWorld!')
        self.assertEqual(convert_to_camel_case('hello   world 123'), 'helloWorld123')
        self.assertEqual(convert_to_camel_case('hello   world 123 '), 'helloWorld123')
        self.assertEqual(convert_to_camel_case(' hello   world 123 '), 'helloWorld123')

if __name__ == '__main__':
    unittest.main()