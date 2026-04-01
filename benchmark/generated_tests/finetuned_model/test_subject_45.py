import unittest

class TestFormatRepeatedString(unittest.TestCase):

    # Test case to check if the function correctly formats the string when n is greater than 1
    def test_format_repeated_string_with_multiple_repetitions(self):
        # Arrange
        string = 'yo'
        n = 3
        expected_output = '"yo" repeated 3 times is: "yoyoyo"'

        # Act
        actual_output = format_repeated_string(string, n)

        # Assert
        self.assertEqual(actual_output, expected_output)

    # Test case to check if the function correctly formats the string when n is 1
    def test_format_repeated_string_with_single_repetition(self):
        # Arrange
        string = 'yo'
        n = 1
        expected_output = '"yo" repeated 1 times is: "yo"'

        # Act
        actual_output = format_repeated_string(string, n)

        # Assert
        self.assertEqual(actual_output, expected_output)

    # Test case to check if the function correctly formats the string when n is 0
    def test_format_repeated_string_with_zero_repetitions(self):
        # Arrange
        string = 'yo'
        n = 0
        expected_output = '"yo" repeated 0 times is: ""'

        # Act
        actual_output = format_repeated_string(string, n)

        # Assert
        self.assertEqual(actual_output, expected_output)

    # Test case to check if the function correctly formats the string when n is a large number
    def test_format_repeated_string_with_large_repetitions(self):
        # Arrange
        string = 'WuB'
        n = 6
        expected_output = '"WuB" repeated 6 times is: "WuBWuBWuBWuBWuBWuB"'

        # Act
        actual_output = format_repeated_string(string, n)

        # Assert
        self.assertEqual(actual_output, expected_output)

    # Test case to check if the function correctly formats the string when n is a negative number
    def test_format_repeated_string_with_negative_repetitions(self):
        # Arrange
        string = 'yo'
        n = -3
        expected_output = '"yo" repeated -3 times is: ""'

        # Act
        actual_output = format_repeated_string(string, n)

        # Assert
        self.assertEqual(actual_output, expected_output)