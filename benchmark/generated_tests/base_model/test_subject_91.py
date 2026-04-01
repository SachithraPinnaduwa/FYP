import unittest

class TestReverseString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_two_characters(self):
        self.assertEqual(reverse_string("ab"), "ba")

    def test_odd_number_of_characters(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_even_number_of_characters(self):
        self.assertEqual(reverse_string("world"), "dlrow")

    def test_mixed_case(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_with_special_characters(self):
        self.assertEqual(reverse_string("!@#$%^&*()"), "()*^%$#@!")

    def test_with_numbers(self):
        self.assertEqual(reverse_string("1234567890"), "0987654321")

if __name__ == '__main__':
    unittest.main()