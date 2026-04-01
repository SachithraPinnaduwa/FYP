import unittest

class TestPrimeNumbersFunction(unittest.TestCase):

    # Test case for a range with prime numbers
    def test_prime_numbers_range(self):
        # Arrange
        start = 10
        end = 20
        
        # Act
        result = entrance(start, end)
        
        # Assert
        expected_result = [11, 13, 17, 19]
        self.assertEqual(result, expected_result)

    # Test case for a range with no prime numbers
    def test_no_prime_numbers_range(self):
        # Arrange
        start = 100
        end = 105
        
        # Act
        result = entrance(start, end)
        
        # Assert
        expected_result = []
        self.assertEqual(result, expected_result)

    # Test case for a range with only prime numbers
    def test_only_prime_numbers_range(self):
        # Arrange
        start = 2
        end = 5
        
        # Act
        result = entrance(start, end)
        
        # Assert
        expected_result = [2, 3, 5]
        self.assertEqual(result, expected_result)

    # Test case for a range with a single number
    def test_single_number_range(self):
        # Arrange
        start = 10
        end = 10
        
        # Act
        result = entrance(start, end)
        
        # Assert
        expected_result = []
        self.assertEqual(result, expected_result)

    # Test case for a range with negative numbers
    def test_negative_numbers_range(self):
        # Arrange
        start = -5
        end = 0
        
        # Act
        result = entrance(start, end)
        
        # Assert
        expected_result = [-5, -3, -2]
        self.assertEqual(result, expected_result)