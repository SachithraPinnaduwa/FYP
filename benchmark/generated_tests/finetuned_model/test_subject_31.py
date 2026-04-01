import unittest

class TestMinimumMovesFunction(unittest.TestCase):

    # Test case where the start and end points are not in the same row or column
    def test_different_rows_and_columns(self):
        # Given
        start_x = 1
        start_y = 2
        end_x = 9
        end_y = 8
        
        # When
        result = minimum_moves(start_x, start_y, end_x, end_y)
        
        # Then
        self.assertEqual(result, 1)

    # Test case where the start and end points are in the same row
    def test_same_row(self):
        # Given
        start_x = 1
        start_y = 2
        end_x = 1
        end_y = 5
        
        # When
        result = minimum_moves(start_x, start_y, end_x, end_y)
        
        # Then
        self.assertEqual(result, 2)

    # Test case where the start and end points are in the same column
    def test_same_column(self):
        # Given
        start_x = 1
        start_y = 2
        end_x = 5
        end_y = 2
        
        # When
        result = minimum_moves(start_x, start_y, end_x, end_y)
        
        # Then
        self.assertEqual(result, 2)

    # Test case with the start and end points being the same (should raise an error, but we will not test for that)
    def test_same_point(self):
        # Given
        start_x = 1
        start_y = 2
        end_x = 1
        end_y = 2
        
        # When
        result = minimum_moves(start_x, start_y, end_x, end_y)
        
        # Then
        self.assertEqual(result, 2)

    # Test case with the start and end points in the same row and column
    def test_same_row_and_column(self):
        # Given
        start_x = 1
        start_y = 2
        end_x = 1
        end_y = 2
        
        # When
        result = minimum_moves(start_x, start_y, end_x, end_y)
        
        # Then
        self.assertEqual(result, 2)

    # Test case with the start and end points in the same row and column, but with different start and end points
    def test_same_row_and_column_different_points(self):
        # Given
        start_x = 1
        start_y = 2
        end_x = 1
        end_y = 3
        
        # When
        result = minimum_moves(start_x, start_y, end_x, end_y)
        
        # Then
        self.assertEqual(result, 2)