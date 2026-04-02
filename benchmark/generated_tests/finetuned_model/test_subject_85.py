import unittest

class TestConvertToCamelCase(unittest.TestCase):
    def test_convert_to_camel_case(self):
        self.assertEqual(convert_to_camel_case('Hello World'), 'HelloWorld')
        self.assertEqual(convert_to_camel_case('hello world'), 'HelloWorld')
        self.assertEqual(convert_to_camel_case('Hello   world'), 'HelloWorld')
        self.assertEqual(convert_to_camel_case('   hello   world   '), 'HelloWorld')
        self.assertEqual(convert_to_camel_case('hello world'), 'HelloWorld')
        self.assertEqual(convert_to_camel_case('hello     world'), 'HelloWorld')
        self.assertEqual(convert_to_camel_case('hello world     '), 'HelloWorld')
        self.assertEqual(convert_to_camel_case('     hello world'), 'HelloWorld')
        self.assertEqual(convert_to_camel_case('hello123 world'), 'Hello123World')
        self.assertEqual(convert_to_camel_case('hello!@# world'), 'Hello!@#World')
        self.assertEqual(convert_to_camel_case('hello world!@#'), 'HelloWorld!@#')
        self.assertEqual(convert_to_camel_case('hello123 world!@#'), 'Hello123World!@#')
        self.assertEqual(convert_to_camel_case('hello!@# world123'), 'Hello!@#World123')
        self.assertEqual(convert_to_camel_case('hello123 world!@#123'), 'Hello123World!@#123')
        self.assertEqual(convert_to_camel_case('hello!@#123 world'), 'Hello!@#123World')
        self.assertEqual(convert_to_camel_case('hello!@#123 world123'), 'Hello!@#123World123')
        self.assertEqual(convert_to_camel_case('hello123 world!@#123'), 'Hello123World!@#123')

if __name__ == '__main__':
    unittest.main()