import unittest

class TestSumListRecursive(unittest.TestCase):

    # Test case for an empty list
    def test_empty_list(self):
        # Arrange
        lst = []

        # Act
        result = sum_list_recursive(lst)

        # Assert
        self.assertEqual(result, 0)

    # Test case for a list with one element
    def test_single_element_list(self):
        # Arrange
        lst = [5]

        # Act
        result = sum_list_recursive(lst)

        # Assert
        self.assertEqual(result, 5)

    # Test case for a list with multiple elements
    def test_multiple_element_list(self):
        # Arrange
        lst = [1, 2, 3, 4, 5]

        # Act
        result = sum_list_recursive(lst)

        # Assert
        self.assertEqual(result, 15)

    # Test case for a list with negative numbers
    def test_negative_numbers_list(self):
        # Arrange
        lst = [-5, -4, -3, -2, -1]

        # Act
        result = sum_list_recursive(lst)

        # Assert
        self.assertEqual(result, -15)

    # Test case for a list with mixed positive and negative numbers
    def test_mixed_numbers_list(self):
        # Arrange
        lst = [1, -2, 3, -4, 5]

        # Act
        result = sum_list_recursive(lst)

        # Assert
        self.assertEqual(result, 3)