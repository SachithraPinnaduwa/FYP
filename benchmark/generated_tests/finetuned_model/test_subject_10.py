import unittest

class TestReverseString(unittest.TestCase):

    # Test case with an empty string
    def test_empty_string(self):
        # Input is an empty string
        input_str = ''
        # Expected output is an empty string
        expected_output = ''
        # Assert that the function output matches the expected output
        self.assertEqual(reverse_string(input_str), expected_output)

    # Test case with a string of length 1
    def test_single_character(self):
        # Input is a string of length 1
        input_str = 'a'
        # Expected output is the same string since it's a single character
        expected_output = 'a'
        # Assert that the function output matches the expected output
        self.assertEqual(reverse_string(input_str), expected_output)

    # Test case with a string of length 2
    def test_two_characters(self):
        # Input is a string of length 2
        input_str = 'ab'
        # Expected output is the string in reverse order
        expected_output = 'ba'
        # Assert that the function output matches the expected output
        self.assertEqual(reverse_string(input_str), expected_output)

    # Test case with a string of length 3
    def test_three_characters(self):
        # Input is a string of length 3
        input_str = 'abc'
        # Expected output is the string in reverse order
        expected_output = 'cba'
        # Assert that the function output matches the expected output
        self.assertEqual(reverse_string(input_str), expected_output)

    # Test case with a string of length 10
    def test_ten_characters(self):
        # Input is a string of length 10
        input_str = 'abcdefghij'
        # Expected output is the string in reverse order
        expected_output = 'jihgfedcba'
        # Assert that the function output matches the expected output
        self.assertEqual(reverse_string(input_str), expected_output)

    # Test case with a string of length 1000 (maximum length)
    def test_max_length(self):
        # Input is a string of length 1000
        input_str = 'a' * 1000
        # Expected output is the string in reverse order
        expected_output = 'a' * 1000
        # Assert that the function output matches the expected output
        self.assertEqual(reverse_string(input_str), expected_output)

    # Test case with a string containing duplicate characters
    def test_duplicate_characters(self):
        # Input is a string containing duplicate characters
        input_str = 'aabbcc'
        # Expected output is the string in reverse order
        expected_output = 'cabbca'
        # Assert that the function output matches the expected output
        self.assertEqual(reverse_string(input_str), expected_output)

    # Test case with a string containing spaces
    def test_string_with_spaces(self):
        # Input is a string containing spaces
        input_str = 'hello world'
        # Expected output is the string in reverse order
        expected_output = 'dlrow olleh'
        # Assert that the function output matches the expected output
        self.assertEqual(reverse_string(input_str), expected_output)