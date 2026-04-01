import unittest

class TestReverseString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_multiple_characters(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_mixed_case(self):
        self.assertEqual(reverse_string("Hello World!"), "!dlroW olleH")

    def test_unicode_characters(self):
        self.assertEqual(reverse_string("Python\u03A9"), "\u03A9nohtyP")

    def test_whitespace(self):
        self.assertEqual(reverse_string(" "), " ")

    def test_numbers(self):
        self.assertEqual(reverse_string("12345"), "54321")

    def test_special_characters(self):
        self.assertEqual(reverse_string("!@#$%^&*()"), ")(&*^%$#@!")

if __name__ == '__main__':
    unittest.main()