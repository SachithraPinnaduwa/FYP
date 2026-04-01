import unittest

class TestFilterStringsFunction(unittest.TestCase):
    def test_filter_strings_with_valid_input(self):
        # Test case with valid input
        data = ["apple", "Banana", "cherry", "Date", "elderberry"]
        n = 5
        expected_output = ["Banana", "elderberry"]
        self.assertEqual(filter_strings(data, n), expected_output)

    def test_filter_strings_with_no_uppercase(self):
        # Test case with no uppercase letters in strings longer than n
        data = ["apple", "banana", "cherry", "date", "elderberry"]
        n = 5
        expected_output = []
        self.assertEqual(filter_strings(data, n), expected_output)

    def test_filter_strings_with_strings_equal_to_n(self):
        # Test case with strings equal to n
        data = ["apple", "Banana", "cherry", "Date", "elderberry"]
        n = 5
        expected_output = ["Banana"]
        self.assertEqual(filter_strings(data, n), expected_output)

    def test_filter_strings_with_empty_data(self):
        # Test case with empty data
        data = []
        n = 5
        expected_output = []
        self.assertEqual(filter_strings(data, n), expected_output)

    def test_filter_strings_with_single_string(self):
        # Test case with single string
        data = ["Banana"]
        n = 5
        expected_output = ["Banana"]
        self.assertEqual(filter_strings(data, n), expected_output)

    def test_filter_strings_with_all_strings_longer_than_n(self):
        # Test case with all strings longer than n
        data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
        n = 5
        expected_output = ["Banana", "Cherry", "Elderberry"]
        self.assertEqual(filter_strings(data, n), expected_output)