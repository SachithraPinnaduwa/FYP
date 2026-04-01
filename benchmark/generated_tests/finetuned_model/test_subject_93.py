import unittest

class TestCountValidAndPairs(unittest.TestCase):

    # Test case for a simple array with repeated elements
    def test_repeated_elements(self):
        A = [1, 1, 1, 1, 1]
        self.assertEqual(count_valid_and_pairs(A), 10)

    # Test case for an array with a single element
    def test_single_element(self):
        A = [10]
        self.assertEqual(count_valid_and_pairs(A), 0)

    # Test case for an array with unique elements
    def test_unique_elements(self):
        A = [1, 2, 3, 4, 5]
        self.assertEqual(count_valid_and_pairs(A), 5)

    # Test case for an array with a large number of elements
    def test_large_array(self):
        A = [100] * 100
        self.assertEqual(count_valid_and_pairs(A), 5050)

    # Test case for an array with a mix of small and large numbers
    def test_mixed_numbers(self):
        A = [1, 2, 3, 4, 5, 100, 200, 300]
        self.assertEqual(count_valid_and_pairs(A), 15)

    # Test case for an array with a single pair of elements that satisfy the condition
    def test_single_pair(self):
        A = [1, 2]
        self.assertEqual(count_valid_and_pairs(A), 1)

    # Test case for an array with a single element that satisfies the condition
    def test_single_element_satisfies(self):
        A = [1]
        self.assertEqual(count_valid_and_pairs(A), 0)