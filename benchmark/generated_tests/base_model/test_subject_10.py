import unittest

class TestReverseString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_string(''), '')

    def test_single_character(self):
        self.assertEqual(reverse_string('a'), 'a')

    def test_multiple_characters(self):
        self.assertEqual(reverse_string('hello'), 'olleh')

    def test_duplicate_characters(self):
        self.assertEqual(reverse_string('racecar'), 'racecar')

    def test_long_string(self):
        long_string = 'abcdefghijklmnopqrstuvwxyz'
        reversed_string = 'zyxwvutsrqponmlkjihgfedcba'
        self.assertEqual(reverse_string(long_string), reversed_string)

    def test_mixed_case(self):
        # Note: This case is not allowed by problem description but included for completeness
        self.assertEqual(reverse_string('Python3.8'), '8.3nohtyP')

if __name__ == '__main__':
    unittest.main()