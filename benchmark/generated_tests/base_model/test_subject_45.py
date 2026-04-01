import unittest

def format_repeated_string(string, n):
    return '"{}" repeated {} times is: "{}"'.format(string, n, string * n)

class TestFormatRepeatedString(unittest.TestCase):

    def test_single_character(self):
        self.assertEqual(format_repeated_string('a', 1), '"a" repeated 1 times is: "a"')

    def test_multiple_characters(self):
        self.assertEqual(format_repeated_string('hello', 2), '"hello" repeated 2 times is: "hellohello"')

    def test_empty_string(self):
        self.assertEqual(format_repeated_string('', 5), '"" repeated 5 times is: ""')

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            format_repeated_string('test', -1)

    def test_zero_times(self):
        self.assertEqual(format_repeated_string('test', 0), '"test" repeated 0 times is: ""')

    def test_space_character(self):
        self.assertEqual(format_repeated_string(' ', 4), '" " repeated 4 times is: "    "')

    def test_punctuation(self):
        self.assertEqual(format_repeated_string('.', 3), '".." repeated 3 times is: "... ..."')

    def test_special_characters(self):
        self.assertEqual(format_repeated_string('@#$', 2), '"@#$" repeated 2 times is: "@#$@#$"')

    def test_long_string(self):
        long_string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        self.assertEqual(format_repeated_string(long_string, 2), f'"{long_string}" repeated 2 times is: "{long_string}{long_string}"')

if __name__ == '__main__':
    unittest.main()