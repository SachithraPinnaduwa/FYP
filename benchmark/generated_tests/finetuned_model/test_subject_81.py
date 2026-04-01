import unittest

class TestFindMinNumber(unittest.TestCase):
    # Test case for a simple test case where the original number is changed
    def test_simple_change(self):
        # Given
        N = "35"
        d = "4"
        expected_output = "34"
        
        # When
        result = find_min_number(N, d)
        
        # Then
        self.assertEqual(result, expected_output)

    # Test case for a test case where the original number remains the same
    def test_no_change(self):
        # Given
        N = "24"
        d = "9"
        expected_output = "24"
        
        # When
        result = find_min_number(N, d)
        
        # Then
        self.assertEqual(result, expected_output)

    # Test case for a test case where the original number is a single digit
    def test_single_digit(self):
        # Given
        N = "5"
        d = "4"
        expected_output = "4"
        
        # When
        result = find_min_number(N, d)
        
        # Then
        self.assertEqual(result, expected_output)

    # Test case for a test case where the original number is a large number
    def test_large_number(self):
        # Given
        N = "1234567890123456789"
        d = "0"
        expected_output = "1234567890123456789"
        
        # When
        result = find_min_number(N, d)
        
        # Then
        self.assertEqual(result, expected_output)

    # Test case for a test case where the original number has multiple occurrences of the digit to be replaced
    def test_multiple_occurrences(self):
        # Given
        N = "5454"
        d = "4"
        expected_output = "44"
        
        # When
        result = find_min_number(N, d)
        
        # Then
        self.assertEqual(result, expected_output)