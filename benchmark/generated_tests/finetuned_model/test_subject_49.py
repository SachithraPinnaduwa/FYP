import unittest

class TestFindMedianFunction(unittest.TestCase):

    # Test case with an odd number of elements
    def test_odd_number_of_elements(self):
        # Arrange
        arr = [1, 3, 3, 6, 7, 8, 9]
        expected_result = 6
        
        # Act
        result = find_median(arr)
        
        # Assert
        self.assertEqual(result, expected_result)

    # Test case with an even number of elements
    def test_even_number_of_elements(self):
        # Arrange
        arr = [1, 2, 3, 4, 5, 6]
        expected_result = 3
        
        # Act
        result = find_median(arr)
        
        # Assert
        self.assertEqual(result, expected_result)

    # Test case with an empty array
    def test_empty_array(self):
        # Arrange
        arr = []
        expected_result = 0  # Assuming the function returns 0 for an empty array
        
        # Act
        result = find_median(arr)
        
        # Assert
        self.assertEqual(result, expected_result)

    # Test case with a single element array
    def test_single_element_array(self):
        # Arrange
        arr = [5]
        expected_result = 5
        
        # Act
        result = find_median(arr)
        
        # Assert
        self.assertEqual(result, expected_result)

    # Test case with an array of duplicates
    def test_array_of_duplicates(self):
        # Arrange
        arr = [3, 3, 3, 3, 3]
        expected_result = 3
        
        # Act
        result = find_median(arr)
        
        # Assert
        self.assertEqual(result, expected_result)

    # Test case with a large array
    def test_large_array(self):
        # Arrange
        arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        expected_result = 550
        
        # Act
        result = find_median(arr)
        
        # Assert
        self.assertEqual(result, expected_result)