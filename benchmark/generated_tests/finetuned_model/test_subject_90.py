import unittest

class TestTransformArrayAfterOperations(unittest.TestCase):

    # Test case with example from problem statement
    def test_example(self):
        a = [-4, 0, -1, 0]
        k = 2
        expected_output = [0, 4, 3, 4]
        self.assertEqual(transform_array_after_operations(a, k), expected_output)

    # Test case with example from problem statement
    def test_example_2(self):
        a = [0, -1, 0, 0, -1, -1, -1, -1, 1, -1]
        k = 1
        expected_output = [1, 2, 1, 1, 2, 2, 2, 2, 0, 2]
        self.assertEqual(transform_array_after_operations(a, k), expected_output)

    # Test case with array having only one element
    def test_single_element_array(self):
        a = [5]
        k = 100000
        expected_output = [5]
        self.assertEqual(transform_array_after_operations(a, k), expected_output)

    # Test case with array having all zeros
    def test_all_zeros_array(self):
        a = [0, 0, 0, 0]
        k = 100
        expected_output = [0, 0, 0, 0]
        self.assertEqual(transform_array_after_operations(a, k), expected_output)

    # Test case with array having all negative elements
    def test_all_negative_array(self):
        a = [-1, -2, -3, -4]
        k = 10
        expected_output = [1, 2, 3, 4]
        self.assertEqual(transform_array_after_operations(a, k), expected_output)

    # Test case with k = 0
    def test_k_zero(self):
        a = [1, 2, 3, 4]
        k = 0
        expected_output = [1, 2, 3, 4]
        self.assertEqual(transform_array_after_operations(a, k), expected_output)

    # Test case with k = 1 and array having duplicates
    def test_k_one_duplicates(self):
        a = [1, 2, 2, 1]
        k = 1
        expected_output = [0, 1, 1, 0]
        self.assertEqual(transform_array_after_operations(a, k), expected_output)

    # Test case with k = 1 and array having negative duplicates
    def test_k_one_negative_duplicates(self):
        a = [-1, -2, -2, -1]
        k = 1
        expected_output = [2, 3, 3, 2]
        self.assertEqual(transform_array_after_operations(a, k), expected_output)