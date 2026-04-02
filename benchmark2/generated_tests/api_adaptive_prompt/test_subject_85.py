from subject_85 import *

import unittest

class TestConvertToCamelCase(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(convert_to_camel_case("hello world"), "HelloWorld")
        self.assertEqual(convert_to_camel_case("hello_world"), "HelloWorld")
        self.assertEqual(convert_to_camel_case("hello-world"), "HelloWorld")
        self.assertEqual(convert_to_camel_case("helloWorld"), "HelloWorld")
        self.assertEqual(convert_to_camel_case("HelloWorld"), "HelloWorld")
        self.assertEqual(convert_to_camel_case("hello wOrLD"), "HelloWorld")
        self.assertEqual(convert_to_camel_case("hello wOrLD!@#"), "HelloWorld")
        self.assertEqual(convert_to_camel_case("hello wOrLD123"), "HelloWorld")
        self.assertEqual(convert_to_camel_case("hello wOrLD!@#123"), "HelloWorld")
        self.assertEqual(convert_to_camel_case("hello wOrLD!@#123 "), "HelloWorld")

if __name__ == '__main__':
    unittest.main()