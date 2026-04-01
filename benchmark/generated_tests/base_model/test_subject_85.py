import unittest

class TestConvertToCamelCase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(convert_to_camel_case(""), "")

    def test_single_word(self):
        self.assertEqual(convert_to_camel_case("hello"), "Hello")

    def test_multiple_words(self):
        self.assertEqual(convert_to_camel_case("hello world"), "HelloWorld")

    def test_leading_space(self):
        self.assertEqual(convert_to_camel_case(" hello"), "Hello")

    def test_trailing_space(self):
        self.assertEqual(convert_to_camel_case("hello "), "Hello")

    def test_consecutive_spaces(self):
        self.assertEqual(convert_to_camel_case("hello  world"), "HelloWorld")

    def test_special_characters(self):
        self.assertEqual(convert_to_camel_case("hello-world"), "HelloWorld")
        self.assertEqual(convert_to_camel_case("hello_world"), "HelloWorld")
        self.assertEqual(convert_to_camel_case("hello.world"), "HelloWorld")

    def test_numbers(self):
        self.assertEqual(convert_to_camel_case("hello123world"), "Hello123World")

    def test_all_uppercase(self):
        self.assertEqual(convert_to_camel_case("HELLO WORLD"), "HelloWorld")

    def test_all_lowercase(self):
        self.assertEqual(convert_to_camel_case("hello world"), "HelloWorld")

if __name__ == '__main__':
    unittest.main()