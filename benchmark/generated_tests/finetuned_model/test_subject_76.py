import unittest

class TestMaxTowerHeight(unittest.TestCase):
    # Test case with the example provided in the problem statement
    def test_example1(self):
        # Define the input parameters
        n = 3
        rings = [(1, 5, 1), (2, 6, 2), (3, 7, 3)]
        # Call the function and store the result
        result = max_tower_height(n, rings)
        # Assert that the result is as expected
        self.assertEqual(result, 6)

    # Test case with the second example provided in the problem statement
    def test_example2(self):
        # Define the input parameters
        n = 4
        rings = [(1, 2, 1), (1, 3, 3), (4, 6, 2), (5, 7, 1)]
        # Call the function and store the result
        result = max_tower_height(n, rings)
        # Assert that the result is as expected
        self.assertEqual(result, 4)

    # Test case with a single ring
    def test_single_ring(self):
        # Define the input parameters
        n = 1
        rings = [(1, 5, 1)]
        # Call the function and store the result
        result = max_tower_height(n, rings)
        # Assert that the result is as expected
        self.assertEqual(result, 1)

    # Test case with multiple rings of the same height
    def test_multiple_rings_same_height(self):
        # Define the input parameters
        n = 3
        rings = [(1, 5, 1), (2, 5, 1), (3, 5, 1)]
        # Call the function and store the result
        result = max_tower_height(n, rings)
        # Assert that the result is as expected
        self.assertEqual(result, 1)

    # Test case with multiple rings of the same height and different radii
    def test_multiple_rings_same_height_different_radii(self):
        # Define the input parameters
        n = 3
        rings = [(1, 5, 1), (2, 5, 1), (3, 6, 1)]
        # Call the function and store the result
        result = max_tower_height(n, rings)
        # Assert that the result is as expected
        self.assertEqual(result, 1)

    # Test case with multiple rings of different heights
    def test_multiple_rings_different_heights(self):
        # Define the input parameters
        n = 3
        rings = [(1, 5, 1), (2, 6, 2), (3, 7, 3)]
        # Call the function and store the result
        result = max_tower_height(n, rings)
        # Assert that the result is as expected
        self.assertEqual(result, 6)